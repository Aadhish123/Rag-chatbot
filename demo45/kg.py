import pdfplumber
import networkx as nx
import matplotlib.pyplot as plt


pdf_text = ""
with pdfplumber.open("1. Deloitte - tax - indiahighlights - 2025.pdf") as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        if text:
            pdf_text += text.lower()

KG = nx.DiGraph()



if "corporate tax" in pdf_text:
    KG.add_node("Corporate Tax", type="TaxType")
    KG.add_node("India", type="Country")
    KG.add_edge("India", "Corporate Tax", relation="HAS_TAX")

if "22%" in pdf_text:
    KG.add_node("22%", type="Rate")
    KG.add_edge("Corporate Tax", "22%", relation="HAS_RATE")

if "domestic companies" in pdf_text:
    KG.add_node("Domestic Company", type="CompanyType")
    KG.add_edge("Corporate Tax", "Domestic Company", relation="APPLICABLE_TO")


pos = nx.spring_layout(KG, k=1)
nx.draw(KG, pos, with_labels=True, node_color="lightgreen", node_size=3000)
edge_labels = nx.get_edge_attributes(KG, "relation")
nx.draw_networkx_edge_labels(KG, pos, edge_labels=edge_labels)

plt.title("Knowledge Graph extracted from PDF")
plt.show()
