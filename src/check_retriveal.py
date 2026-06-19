import os
import chromadb
# from dotenv import load_dotenv
# from langchain_openai import OpenAIEmbeddings

# load_dotenv()

embedder = OpenAIEmbeddings(model="text-embedding-3-small")

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection("zudyog_products")

results = collection.query(
    query_embeddings=[
        embedder.embed_query("Does the silk saree need dry cleaning?")
    ],
    n_results=2,
    include=["documents", "metadatas", "distances"],
)

for doc, meta in zip(
    results["documents"][0],
    results["metadatas"][0]
):
    print(f"[{meta['chunk_type']}] {doc[:80]}...")