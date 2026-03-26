import chromadb
from chromadb.config import Settings

# Initialize Chroma client (auto-persistent in new versions)
client = chromadb.Client(
    Settings(
        persist_directory="chroma_db"
    )
)

# Create or get collection
collection = client.get_or_create_collection(name="documents")


def add_documents(chunks, embeddings):
    ids = [f"{chunk['doc_id']}_{chunk['chunk_id']}" for chunk in chunks]
    documents = [chunk["text"] for chunk in chunks]
    metadatas = [{"doc_id": chunk["doc_id"]} for chunk in chunks]

    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas
    )

    # Debug log
    print(f"Stored {len(chunks)} chunks. Total in DB: {collection.count()}")


def query_documents(query_embedding, top_k=3):
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results
