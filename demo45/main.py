import os
from database import engine
from models import Base
from document_registry import register_document
from chunking import process_document
from vector_index import build_vector_index

UPLOAD_DIR = "uploads"

# Create tables
Base.metadata.create_all(bind=engine)

# Phase 1 & 2: Register and chunk ALL PDFs dynamically
for file in os.listdir(UPLOAD_DIR):
    if file.lower().endswith(".pdf"):
        pdf_path = os.path.join(UPLOAD_DIR, file)
        print(f"Processing PDF: {pdf_path}")

        doc = register_document(pdf_path)
        print("Document registered:", doc.id)

        process_document(doc)
        print("Chunking completed")

# Phase 3: Build vector index once
build_vector_index()
print("Vector index built successfully")
