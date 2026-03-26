from typing import List, Dict


def chunk_text(
    text: str,
    chunk_size: int = 500,
    overlap: int = 50,
    doc_id: str = "unknown"
) -> List[Dict]:
    chunks = []
    start = 0
    chunk_id = 0

    while start < len(text):
        end = start + chunk_size
        chunk_content = text[start:end]

        chunks.append({
            "chunk_id": chunk_id,
            "doc_id": doc_id,
            "text": chunk_content
        })

        chunk_id += 1
        start += chunk_size - overlap

    return chunks
