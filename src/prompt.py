from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage


from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))
from src.retriever import retrieve

llm = ChatOllama(
    model="llama3.2",  
    temperature=0,
)

SHOPBOT_SYSTEM = """
You are ShopBot, a warm and knowledgeable product assistant for zUdyog Fashion —
an Indian fashion e-commerce store specialising in kurtas, sarees,
anarkali suits, and contemporary Indian fashion.

YOUR ONLY SOURCE OF TRUTH is the Product Information provided below.
You have no other knowledge about zUdyog's products.

When you have the information:
- Answer directly and specifically.
- Include relevant details: size, colour, price, occasion suitability,
  care instructions.
- Be warm and conversational.
- If multiple products are relevant, mention all of them briefly.

When you do NOT have the information:
- Say exactly:
  "I don't have that specific information. Please reach our support team
  at support@zudyog.in for help."
- Do not guess.
- Do not approximate.
- Do not use fashion industry knowledge to fill gaps.

Product Information:

{context}
"""


def answer(query: str) -> str:

    evidence = retrieve(query)

    if evidence is None:
        return (
            "I don't have a product that matches that specifically. "
            "Could you describe what you're looking for differently, "
            "or contact our team at support@zudyog.in?"
        )

    context = "\n\n---\n\n".join(
        f"[{e['metadata']['chunk_type'].upper()}]\n{e['text']}"
        for e in evidence
    )

    messages = [
        SystemMessage(
            content=SHOPBOT_SYSTEM.format(context=context)
        ),
        HumanMessage(content=query),
    ]

    response = llm.invoke(messages)

    return response.content