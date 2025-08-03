from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import simpleSplit

def export_to_pdf(filename, qa_pairs, similar_qa_pairs=None):
    """
    Creates a PDF with clearly separated questions and answers.
    
    Args:
        filename (str): Output PDF file name
        qa_pairs (list of tuples): List like [(question, answer), ...]
        similar_qa_pairs (list of tuples, optional): List of similar questions and answers.
    """
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    y = height - 50
    c.setFont("Helvetica", 12)
    max_width = width - 100  # Leave margin on both sides

    for idx, (question, answer) in enumerate(qa_pairs, 1):
        # Wrap question text
        question_lines = simpleSplit(f"Q{idx}. {question}", "Helvetica", 12, max_width)
        for line in question_lines:
            if y < 50:
                c.showPage()
                y = height - 50
                c.setFont("Helvetica", 12)
            c.drawString(50, y, line)
            y -= 20

        y -= 10  # small space after main question

        # Add "Ans:" before the answer
        answer_text = f"Ans: {answer}"
        answer_lines = simpleSplit(answer_text, "Helvetica", 12, max_width)

        for line in answer_lines:
            if y < 50:
                c.showPage()
                y = height - 50
                c.setFont("Helvetica", 12)
            c.drawString(50, y, line)
            y -= 20

        y -= 40  # Two-line space after each main Q&A pair

    if similar_qa_pairs:
        y -= 20
        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, y, "Similar Questions and Answers")
        y -= 30
        c.setFont("Helvetica", 12)

        for idx, (question, answer) in enumerate(similar_qa_pairs, 1):
            # Wrap question text
            question_lines = simpleSplit(f"Q{idx}. {question}", "Helvetica", 12, max_width)
            for line in question_lines:
                if y < 50:
                    c.showPage()
                    y = height - 50
                    c.setFont("Helvetica", 12)
                c.drawString(50, y, line)
                y -= 20

            y -= 10  # small space after main question

            # Add "Ans:" before the answer
            answer_text = f"Ans: {answer}"
            answer_lines = simpleSplit(answer_text, "Helvetica", 12, max_width)

            for line in answer_lines:
                if y < 50:
                    c.showPage()
                    y = height - 50
                    c.setFont("Helvetica", 12)
                c.drawString(50, y, line)
                y -= 20

            y -= 40  # Two-line space after each main Q&A pair

    c.save()
