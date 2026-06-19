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

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

from data.products import PRODUCTS
from src.chunker import product_to_chunks


all_chunks = []

for product in PRODUCTS:
    chunks = product_to_chunks(product)
    all_chunks.extend(chunks)

    print(f"{product['name']}: {len(chunks)} chunks")


print(f"\nTotal chunks to embed: {len(all_chunks)}")

texts = [c["text"] for c in all_chunks]
vectors = embeddings_model.embed_documents(texts)
collection.add(
ids=[c["id"] for c in all_chunks],
embeddings=vectors,
documents=texts,
metadatas=[c["metadata"] for c in all_chunks],
)
print(f"Ingested {collection.count()} chunks into ChromaDB.")

# products = [
# {
#     "id": "p001",
#     "text": "Cotton kurta. Breathable, ideal for summer. White, sky blue, "
#     "mint green. Sizes S to XXL. Machine washable. Price ₹1,299.",
#     "metadata": {"category": "kurta", "season": "summer", "price": 1299},
# },
# {
#     "id": "p002",
#     "text": "Woolen shawl. Heavyweight, warm, ideal for winter evenings. "
#     "Charcoal grey and maroon. One size. Dry clean only. Price ₹2,199.",
#     "metadata": {"category": "shawl", "season": "winter", "price": 2199},
# },
# {
#     "id": "p003",
#     "text": "Silk saree with zari border. Festive wear. Red, gold, emerald. "
#     "Dry clean only. Price ₹4,299.",
#     "metadata": {"category": "saree", "occasion": "festive", "price": 4299},
# },
# {
#     "id": "p004",
#     "text": "Linen co-ord set. Relaxed fit, summer casual. Beige, sage, "
#     "dusty rose. Sizes XS to XL. Price ₹1,899.",
#     "metadata": {"category": "coord-set", "season": "summer", "price": 1899},
# },
# {
#     "id": "p005",
#     "text": "Anarkali suit with dupatta. Embroidered, festive. Teal. "
#     "Sizes S to XXL. Price ₹3,499.",
#     "metadata": {"category": "suit", "occasion": "festive", "price": 3499},
# },

# {
#     "id": "p006",
#     "text": "A pair of denim jeans. Casual wear, year-round. Classic blue. ",
#     "metadata": {"category": "jeans", "price": 1499},
# }
# ]

# texts = [p["text"] for p in products]
# vectors = embeddings_model.embed_documents(texts)

# collection.add(
#     ids=[p["id"] for p in products],
#     embeddings=vectors,
#     documents=texts,
#     metadatas=[p["metadata"] for p in products],
# )

# print(f"Ingested {collection.count()} products into ChromaDB.")
