import pdfplumber
from models import DocumentChunk
from database import SessionLocal

def chunk_text(text, max_words=200):
    words = text.split()
    return [" ".join(words[i:i+max_words]) for i in range(0, len(words), max_words)]

def process_document(document):
    db = SessionLocal()

    with pdfplumber.open(document.file_path) as pdf:
        for page_index, page in enumerate(pdf.pages):
            text = page.extract_text()
            if not text:
                continue

            chunks = chunk_text(text)

            for idx, chunk in enumerate(chunks):
                db.add(DocumentChunk(
                    document_id=document.id,
                    page_number=page_index + 1,
                    chunk_index=idx,
                    chunk_text=chunk
                ))

    db.commit()
    db.close()
