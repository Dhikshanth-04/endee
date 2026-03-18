from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

texts = []
embeddings = []

def store_insight(text):
    try:
        emb = model.encode(text)
        texts.append(text)
        embeddings.append(emb)
        return "stored (vector)"
    except Exception as e:
        return f"error: {str(e)}"


def search_insights(query):
    if not texts:
        return []

    query_emb = model.encode(query)

    similarities = []
    for emb in embeddings:
        sim = np.dot(query_emb, emb) / (np.linalg.norm(query_emb) * np.linalg.norm(emb))
        similarities.append(sim)

    top_indices = np.argsort(similarities)[-3:][::-1]

    return [texts[i] for i in top_indices]


def get_all_insights():
    return texts