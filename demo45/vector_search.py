from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle

def semantic_search(query, top_k=3):
    model = SentenceTransformer("all-MiniLM-L6-v2")

    index = faiss.read_index("vector.index")
    with open("vector_metadata.pkl", "rb") as f:
        metadata = pickle.load(f)

    query_embedding = model.encode([query])
    D, I = index.search(np.array(query_embedding), top_k)

    results = []
    for idx in I[0]:
        results.append(metadata[idx])

    return results
