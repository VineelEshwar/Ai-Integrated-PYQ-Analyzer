import pytesseract
from PIL import Image, UnidentifiedImageError
import pdfplumber
import os

def extract_text_from_image(img_path: str) -> str:
    try:
        if not os.path.exists(img_path):
            raise FileNotFoundError(f"Image not found: {img_path}")

        image = Image.open(img_path)
        if image.mode != 'RGB':
            image = image.convert('RGB')

        text = pytesseract.image_to_string(image)
        return text.strip()

    except UnidentifiedImageError:
        return "⚠️ Cannot open image file. Please upload a valid image."
    except Exception as e:
        return f"⚠️ OCR failed: {e}"

def extract_text_from_pdf(pdf_path: str) -> str:
    try:
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"PDF not found: {pdf_path}")

        text = ""
        with pdfplumber.open(pdf_path) as pdf:
            for i, page in enumerate(pdf.pages):
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
                else:
                    text += f"\n[⚠️ Page {i+1} had no extractable text]\n"
        return text.strip()

    except Exception as e:
        return f"⚠️ PDF text extraction failed: {e}"
