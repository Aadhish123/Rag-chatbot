from ctransformers import AutoModelForCausalLM
import os

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "models",
    "llama-3.1-8b-instruct.Q4_K_M.gguf"
)

llm = AutoModelForCausalLM.from_pretrained(
    MODEL_PATH,
    model_type="llama",
    local_files_only=True
)

def generate_answer(context, question):
    prompt = f"""
You are a factual assistant.
Answer ONLY using the context below.
If the answer is not present, say "Not found".

Context:
{context}

Question:
{question}

Answer:
"""
    return llm(prompt, max_new_tokens=200).strip()
