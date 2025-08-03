
#  AI-Powered Previous Year Question Assistant

This project is a smart assistant built with Streamlit and OCR + AI models to work with previous year question papers (PYQs).

---

##  Features

1.  **Upload PYQ papers (PDF or Image)** to:
   - Get direct **answers** using AI
   - Generate **similar questions**

2.  API key support via `.env` file  
   - Add your key like: `API_KEY=your_key_here`

3.  Uses **Tesseract OCR** to extract text from scanned images or PDFs

4.  **Text-to-Speech** functionality using `pyttsx3`  
   - Hear answers or hints spoken aloud

5.  **Downloadable** Q&A outputs (optional: as text or PDF)

---

##  How to Run

1.  Install all required packages:

```bash
pip install -r requirements.txt
```

> Make sure the following packages are included:
> - `streamlit`
> - `pytesseract`
> - `pdfplumber`
> - `openai`
> - `pyttsx3`
> - `python-dotenv`

2. Place your API key in a `.env` file:

```
API_KEY=your_api_key_here
```

3. ▶ Launch the app using Streamlit:

```bash
streamlit run app.py
```

Then visit `http://localhost:8501` in your browser.

---

## 📁 Folder Suggestions

HACKATHON/
│
├── app.py                        # Main Streamlit application
├── .env                          # API key configuration
├── exported_qa.pdf               # Output file for exported Q&A
├── requirments.txt               # Python package dependencies (fix typo to "requirements.txt")
│
├── logic/
│   ├── answer_generator.py       # AI answer generation logic
│   ├── pdf_exporter.py           # Exports questions and answers to PDF
│   ├── question_generator.py     # Generates similar questions
│   └── text_to_speech.py         # Converts text to voice using pyttsx3
│
├── ocr/
│   └── extractor.py              # Extracts text from PDFs or images using OCR
│
├── prompts/
│   ├── answer.txt                # Prompt template for answer generation
│   ├── hint.txt                  # Prompt template for hints
│   └── new_question.txt          # Prompt template for similar questions
│
├── static/
│   └── templates/
│       └── index.html            # Optional frontend template (if used)
│
├── utils/
│   ├── gemini.py                 # Gemini API helper (if used)
│   └── preprocess.py             # Cleans text and splits into questions
│
└── venv/                         # Python virtual environment

---



## 💬 Notes

- Make sure Tesseract is installed and added to your system path.
- Compatible with both OpenAI or other LLM APIs if integrated.
- Ideal for exam preparation apps, tutors, and learning platforms.

---


