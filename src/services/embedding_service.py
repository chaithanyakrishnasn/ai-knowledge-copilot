from sentence_transformers import SentenceTransformer

# Load model once (important for performance)
model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_embeddings(texts):
    """
    texts: List[str]
    returns: List[List[float]]
    """
    return model.encode(texts)
