import re

def clean_text(text: str) -> str:
    # Normalize newlines and spaces
    text = re.sub(r'\n+', '\n', text)
    text = re.sub(r'[ \t]+', ' ', text)

    # Remove headers, footers, exam details
    text = re.sub(r'(NP.*?Examination.*?)\n', '', text, flags=re.IGNORECASE)
    text = re.sub(r'(SECTION\s+[A-Z])', r'\n\1\n', text, flags=re.IGNORECASE)
    text = re.sub(r'(Page\s+\d+)', '', text, flags=re.IGNORECASE)
    text = re.sub(r'(Max\. Marks.*?)\n', '', text, flags=re.IGNORECASE)
    text = re.sub(r'(Time.*?)\n', '', text, flags=re.IGNORECASE)

    # Remove stray OCR characters
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)

    return text.strip()

def split_into_questions(text: str):
    # Normalize question prefixes like Q1., Q1), 1. etc.
    text = re.sub(r'(\n|^)\s*(Q?\d{1,3})[\.\)]\s+', r'\n\2. ', text)

    # Split based on numbering
    parts = re.split(r'\n(Q?\d{1,3})\.\s+', text)

    questions = []
    for i in range(1, len(parts), 2):
        number = parts[i]
        question = parts[i+1]

        # Optional: Clean question text
        question = question.strip().replace('\n', ' ')

        # Look for sub-questions (like a), b), etc.)
        sub_qs = re.findall(r'([a-eA-E][\.\)]\s.*?)(?=(?: [a-eA-E][\.\)])|$)', question, flags=re.DOTALL)

        if sub_qs:
            for sub in sub_qs:
                sub = sub.strip().replace('\n', ' ')
                questions.append(f"{number}.{sub}")
        else:
            full_q = f"{number}. {question}"
            questions.append(full_q)

    return questions
