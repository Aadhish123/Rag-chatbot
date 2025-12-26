import networkx as nx
from database import SessionLocal
from models import DocumentChunk
from vector_search import semantic_search
import matplotlib.pyplot as plt
from llm_generator import generate_answer


# -----------------------------
# Build Knowledge Graph
# -----------------------------
def build_kg():
    KG = nx.DiGraph()

    # Corporate Tax
    KG.add_edge("India", "Corporate Tax", relation="HAS_TAX")
    KG.add_edge("Corporate Tax", "22%", relation="HAS_RATE")
    KG.add_edge("Corporate Tax", "Domestic Company", relation="APPLICABLE_TO")

    # GST
    KG.add_edge("India", "GST", relation="HAS_TAX")
    KG.add_edge("GST", "18%", relation="HAS_RATE")

    # Capital Gains Tax
    KG.add_edge("India", "Capital Gains Tax", relation="HAS_TAX")
    KG.add_edge("Capital Gains Tax", "12.5%", relation="HAS_RATE")

    return KG


# -----------------------------
# Fetch chunk from DB
# -----------------------------
def get_chunk(chunk_id):
    db = SessionLocal()
    chunk = db.query(DocumentChunk).filter_by(id=chunk_id).first()
    db.close()
    return chunk


# -----------------------------
# Grounded Answer Logic
# -----------------------------
def grounded_answer(query):
    KG = build_kg()
    results = semantic_search(query)

    for res in results:
        chunk = get_chunk(res["chunk_id"])
        if not chunk:
            continue

        text = chunk.chunk_text.lower()

        # GST
        if "gst" in text and KG.has_edge("GST", "18%"):
            return {
                "answer": "GST rate in India is 18%",
                "document_id": res["document_id"],
                "page_number": res["page_number"]
            }

        # Capital Gains
        if "capital gains" in text and KG.has_edge("Capital Gains Tax", "12.5%"):
            return {
                "answer": "Capital gains tax rate in India is 12.5%",
                "document_id": res["document_id"],
                "page_number": res["page_number"]
            }

        # Corporate Tax
        if "corporate tax" in text and KG.has_edge("Corporate Tax", "22%"):
            return {
                "answer": "Corporate tax rate in India is 22%",
                "document_id": res["document_id"],
                "page_number": res["page_number"]
            }

    return {"answer": "No verified answer found"}


# -----------------------------
# KG Visualization
# -----------------------------
def show_kg():
    KG = build_kg()

    pos = nx.spring_layout(KG, k=1)
    nx.draw(
        KG,
        pos,
        with_labels=True,
        node_color="lightblue",
        node_size=3000
    )

    edge_labels = nx.get_edge_attributes(KG, "relation")
    nx.draw_networkx_edge_labels(KG, pos, edge_labels=edge_labels)

    plt.title("Knowledge Graph (Tax Domain)")
    plt.show()
def grounded_answer(query):
    KG = build_kg()
    results = semantic_search(query)

    for res in results:
        chunk = get_chunk(res["chunk_id"])
        if not chunk:
            continue

        text = chunk.chunk_text.lower()

        # FACT VALIDATION (KG)
        if "corporate tax" in text and KG.has_edge("Corporate Tax", "22%"):
            llm_answer = generate_answer(chunk.chunk_text, query)
            return {
                "answer": llm_answer,
                "document_id": res["document_id"],
                "page_number": res["page_number"]
            }

    return {"answer": "No verified answer found"}
