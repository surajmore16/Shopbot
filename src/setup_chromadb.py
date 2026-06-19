# from dotenv import load_dotenv
# from langchain_openai import OpenAIEmbeddings
# load_dotenv() 
# embeddings = OpenAIEmbeddings()

import chromadb
from langchain_ollama import OllamaEmbeddings
embeddings = OllamaEmbeddings(model="nomic-embed-text")

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="zudyog_products",
    metadata={"hnsw:space": "cosine"}
)

print(f"Collection ready: {collection.name}")
print(f"Documents stored: {collection.count()}")