from utils.gemini import init_gemini
import os

# Initialize model once
model = init_gemini()

def _load_prompt(file_path: str, question: str) -> str:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Prompt file not found: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read().format(question=question)

def get_answer(question: str) -> str:
    try:
        prompt = _load_prompt("prompts/answer.txt", question)
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Failed to generate answer: {e}"

def get_hints(question: str) -> str:
    try:
        prompt = _load_prompt("prompts/hint.txt", question)
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Failed to generate hint: {e}"
