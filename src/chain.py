from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate


from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.retriever import retrieve,get_retriever
from src.prompt import SHOPBOT_SYSTEM


def format_docs(docs: list) -> str:
    if not docs:
        return "No product information available."

    formatted = []

    for i, doc in enumerate(docs, start=1):
        chunk_type = doc.metadata.get("chunk_type", "general")

        formatted.append(
            f"[Item {i} — {chunk_type}]\n{doc.page_content}"
        )

    return "\n\n---\n\n".join(formatted)


def build_chain():
    retriever = get_retriever(k=3)

    llm = ChatOllama(
        model="llama3.2",  
        temperature=0,
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", SHOPBOT_SYSTEM),
            ("human", "{question}"),
        ]
    )

    chain = (
        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough(),
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain

shopbot = build_chain()
test_cases = [
"Does the embroidered anarkali suit come with a dupatta?",
"What is the return policy for the silk saree?",
"Does the cotton kurta shrink after washing?",
"Do you sell men's sherwanis?",
"Does the silk saree come with a blouse?",
]
for question in test_cases:
    print(f"\nCustomer: {question}")
    print(f"ShopBot: {shopbot.invoke(question)}")
    print("-" * 60)