# from dotenv import load_dotenv
# from langchain_openai import OpenAIEmbeddings
# load_dotenv() 
# embeddings = OpenAIEmbeddings()

from langchain_ollama import OllamaEmbeddings
embeddings = OllamaEmbeddings(model="nomic-embed-text")
import numpy as np

products = [
    {
        "id": "p001",
        "text": "Breathable cotton kurta, ideal for summer. "
        "Available in white, sky blue, mint green. Sizes S to XXL. Price ₹1,299."
    },
    {
        "id": "p002",
        "text": "Heavyweight woolen shawl for winter evenings. "
        "Charcoal grey and maroon. One size fits all. Price ₹2,199."
    },
    {
        "id": "p003",
        "text": "Printed silk saree with zari border, festive wear. "
        "Available in red, gold, emerald. Dry clean only. Price ₹4,299."
    },
    {
        "id": "p004",
        "text": "Linen co-ord set, relaxed fit, summer casual. "
        "Colours: beige, sage, dusty rose. Sizes XS to XL. Price ₹1,899."
    },
    {
        "id": "p005",
        "text": "Embroidered anarkali suit with dupatta. "
        "Teal. Sizes S to XXL. Price ₹3,499."
    }
]


# for i, product in enumerate(products):
#     print(f"Product {i+1}: {product['text']}...")  # print first 55 characters of product text


def cosine_similarity(vec1,vec2):
    a = np.array(vec1)
    b = np.array(vec2)
    return float(np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b))) # formula for cosine similarity ie. A.B / ||A|| ||B||

print("Embedding products for vector search...")
product_vectors = embeddings.embed_documents([p["text"] for p in products])

# for i,product in enumerate(products):
#     print(f"Product id {product['id']}\nproduct description : {product["text"]} \nvector of text: {product_vectors[i]}")



test_queries = [
    "light fabric for summer",
    "something warm for cold evenings",
    "festive Indian outfit for a wedding",
    "traditional silk drape for celebration",
    "casual everyday Indian wear",
]


for query in test_queries:
    query_vector = embeddings.embed_query(query)
    scored = []
    for i, product in enumerate(products):
        score = cosine_similarity(query_vector, product_vectors[i])
        scored.append((score, product["id"], product["text"]))

    scored.sort(reverse=True)

    # print("scored :- ",scored)
    print(f"\nQuery: '{query}'")
    print(f" Best match (score {scored[0][0]:.2f}): {scored[0][2]}...")
    print(f" 2nd match (score {scored[1][0]:.2f}): {scored[1][2]}...")
    
queries = [
    "something for a wedding",
    "warm wrap for cold evenings",
    "easy care everyday wear",
]

for query in queries:
    query_vector = embeddings.embed_query(query)
    scored = []
    for i, product in enumerate(products):
        score = cosine_similarity(query_vector, product_vectors[i])
        scored.append((score, product["id"], product["text"]))

    scored.sort(reverse=True)

    # print("scored :- ",scored)
    print(f"\nQuery: '{query}'")
    print(f" Best match (score {scored[0][0]:.2f}): {scored[0][2]}...")
    print(f" 2nd match (score {scored[1][0]:.2f}): {scored[1][2]}...")
