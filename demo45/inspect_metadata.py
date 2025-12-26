import pickle

with open("vector_metadata.pkl", "rb") as f:
    metadata = pickle.load(f)

# Print first 5 entries
for item in metadata[:5]:
    print(item)
