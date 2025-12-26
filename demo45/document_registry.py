import pdfplumber
from models import Document
from database import SessionLocal

def register_document(file_path):
    with pdfplumber.open(file_path) as pdf:
        total_pages = len(pdf.pages)

    db = SessionLocal()
    doc = Document(
        filename=file_path.split("/")[-1],
        file_path=file_path,
        total_pages=total_pages
    )
    db.add(doc)
    db.commit()
    db.refresh(doc)
    db.close()

    return doc
