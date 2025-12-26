from database import SessionLocal
from models import DocumentChunk
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle

def build_vector_index():
    db = SessionLocal()
    chunks = db.query(DocumentChunk).all()
    db.close()

    texts = [c.chunk_text for c in chunks]

    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(texts)

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))

    metadata = [
        {
            "chunk_id": c.id,
            "document_id": c.document_id,
            "page_number": c.page_number
        }
        for c in chunks
    ]

    faiss.write_index(index, "vector.index")

    with open("vector_metadata.pkl", "wb") as f:
        pickle.dump(metadata, f)

    print("Vector index built successfully")
