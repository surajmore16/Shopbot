from langchain_ollama import OllamaEmbeddings
embeddings = OllamaEmbeddings(model="nomic-embed-text")

result = embeddings.embed_query("Does this kurta come in size S?")
print(f"Local setup working.")
print(f"Embedding dimensions: {len(result)}")
print(f"First three values: {result[:3]}")

result2 = embeddings.embed_query("What is the price of the silk saree?")
print(f"\nKurta size question — first 3 values: {result[:3]}")
print(f"Saree price question — first 3 values: {result2[:3]}")