import chromadb
from langchain_ollama import OllamaEmbeddings
from langchain_core.documents import Document
from langchain_core.runnables import RunnableLambda
embeddings_model = OllamaEmbeddings(model="nomic-embed-text")


client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="zudyog_products",
    metadata={"hnsw:space": "cosine"},
)

SIMILARITY_THRESHOLD = 0.75
MAX_RESULTS = 3


def retrieve(
    query: str,
    chunk_type: Optional[str] = None,
    product_id: Optional[str] = None,
    ) -> Optional[list[dict]]:

    query_vector = embeddings_model.embed_query(query)

    where: dict = {}

    if chunk_type:
        where["chunk_type"] = chunk_type

    if product_id:
        where["product_id"] = product_id

    results = collection.query(
        query_embeddings=[query_vector],
        n_results=MAX_RESULTS,
        where=where if where else None,
        include=["documents", "distances", "metadatas"],
    )

    retrieved = []

    for i, doc in enumerate(results["documents"][0]):
        distance = results["distances"][0][i]
        similarity = 1 - distance  # ChromaDB returns distance; convert to similarity

        if similarity >= SIMILARITY_THRESHOLD:
            retrieved.append(
                {
                    "text": doc,
                    "similarity": round(similarity, 4),
                    "metadata": results["metadatas"][0][i],
                }
            )

    return retrieved if retrieved else None


def get_retriever(k=3):

    def _retrieve(query: str):
        results = retrieve(query)

        if not results:
            return []

        return [
            Document(
                page_content=r["text"],
                metadata=r["metadata"]
            )
            for r in results[:k]
        ]

    return RunnableLambda(_retrieve)

def respond(query: str) -> str:

    evidence = retrieve(query)

    if evidence is None:
        return (
            "I don't have a product that matches that specifically. "
            "Could you describe what you're looking for differently, "
            "or contact our team at support@zudyog.in?"
        )

    # Evidence found — Chapter 7 will pass these chunks to the model
    return "\n\n".join(
        [f"[{e['similarity']}] {e['text']}" for e in evidence]
    )


if __name__ == "__main__":
    queries = [
        "do you have anything for a winter wedding?",
        "something light for summer",
        "care instructions for the silk saree",
    ]

    for q in queries:
        print(f"Query: {q}")
        print(respond(q))
        print("")