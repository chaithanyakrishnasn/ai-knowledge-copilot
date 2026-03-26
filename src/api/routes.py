from fastapi import APIRouter, UploadFile, File, HTTPException

from src.core.config import settings
from src.core.logger import logger

from src.services.pdf_service import extract_text_from_pdf
from src.services.chunking_service import chunk_text
from src.services.embedding_service import generate_embeddings
from src.services.llm_service import generate_answer
from src.services.memory_service import (
    add_message,
    get_history,
    clear_history
)

from src.db.vector_store import add_documents, query_documents


router = APIRouter()


# ------------------- BASIC ROUTES -------------------

@router.get("/")
def root():
    return {"message": "AI Knowledge Copilot is running 🚀"}


@router.get("/health")
def health_check():
    return {
        "status": "ok",
        "env": settings.ENV
    }


@router.get("/config-test")
def config_test():
    return {
        "env": settings.ENV,
        "has_api_key": bool(settings.OPENAI_API_KEY)
    }


# ------------------- DOCUMENT INGESTION -------------------

@router.post("/upload-doc")
async def upload_doc(file: UploadFile = File(...)):
    file_path = f"data/{file.filename}"

    # Save file
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    # Extract text
    text = extract_text_from_pdf(file_path)

    # Chunking
    chunks = chunk_text(text, doc_id=file.filename)

    # Embeddings
    chunk_texts = [chunk["text"] for chunk in chunks]
    embeddings = generate_embeddings(chunk_texts)

    # Store in vector DB
    add_documents(chunks, embeddings)

    return {
        "filename": file.filename,
        "num_chunks": len(chunks),
        "status": "stored in vector DB"
    }


# ------------------- ASK (RAG + MEMORY + LOGGING) -------------------

@router.post("/ask")
async def ask_question(query: str):
    if not query.strip():
        raise HTTPException(
            status_code=400,
            detail="Query cannot be empty"
        )

    try:
        # 🔹 1. Log incoming query
        logger.info("Received query: %s", query)

        # Step 1: Embed query
        query_embedding = generate_embeddings([query])[0]

        # Step 2: Retrieve relevant chunks
        results = query_documents(query_embedding)

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]

        # Step 3: Clean + limit context
        documents = [doc.strip() for doc in documents if doc]
        documents = documents[:3]
        metadatas = metadatas[:3]

        # Step 4: Get chat history
        history = get_history()

        # Step 5: Generate answer using LLM
        answer = generate_answer(query, documents, history)

        # 🔹 2. Log success
        logger.info("Answer generated successfully")

        # Step 6: Save conversation
        add_message("user", query)
        add_message("assistant", answer)

        # Step 7: Build source attribution
        sources = []
        for doc, meta in zip(documents, metadatas):
            sources.append({
                "doc_id": meta["doc_id"],
                "content": doc[:300]
            })

        return {
            "query": query,
            "answer": answer,
            "sources": sources
        }

    except Exception as e:
        import traceback
        logger.error("Error occurred:\n%s", traceback.format_exc())

        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        ) from e


# ------------------- MEMORY MANAGEMENT -------------------

@router.post("/clear-history")
def clear_chat():
    clear_history()
    return {"message": "Chat history cleared"}
