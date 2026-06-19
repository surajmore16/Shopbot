# from dotenv import load_dotenv
# from langchain_openai import OpenAIEmbeddings
# load_dotenv() 
# embeddings = OpenAIEmbeddings()

import chromadb
from langchain_ollama import OllamaEmbeddings

embeddings_model = OllamaEmbeddings(model="nomic-embed-text")

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="zudyog_products",
    metadata={"hnsw:space": "cosine"}
)

def search(query: str, n_results: int = 2):
    query_vector = embeddings_model.embed_query(query)

    # results = collection.query(
    #     query_embeddings=[query_vector],
    #     n_results=n_results,
    #     include=["documents", "metadatas", "distances"],
    # )

    results = collection.query(
        query_embeddings=[query_vector],
        n_results=2,
        where={"occasion": "festive"},
    )

    print(f"\nQuery: '{query}'")

    for i, (doc, meta, dist) in enumerate(zip(
        results["documents"][0],
        results["metadatas"][0],
        results["distances"][0],
    )):
        similarity =1-dist # distance is less and similarity is more
        print(f"{i+1}. Similarity is [{similarity:.3f}] for {doc}...")
        print(f"   Category: {meta['category']} | Price: ₹{meta['price']}")

search("light fabric for summer")
search("something warm for cold nights")
search("festive outfit for a wedding reception")
search("under ₹2,000 casual wear")

search("something causal for a day out")
search("under ₹1,500")
search("daily wear for office")