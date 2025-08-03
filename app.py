import streamlit as st
import os

# Custom modules
from ocr.extractor import extract_text_from_pdf, extract_text_from_image
from utils.preprocess import clean_text, split_into_questions
from logic.answer_generator import get_answer, get_hints
from logic.question_generator import generate_similar_question
# Optional features
from logic.text_to_speech import text_to_speech_file
from logic.pdf_exporter import export_to_pdf

st.set_page_config(page_title="Smart Question Paper Assistant", layout="wide")

# Add a clear button to reset the session state
if st.button("Clear"):
    st.session_state.clear()
    st.rerun()

st.title("Smart Question Paper Assistant")

# Sidebar for controls
with st.sidebar:
    st.header("Controls")
    if st.button("Clear Session"):
        st.session_state.clear()
        st.rerun()

    st.session_state.uploaded_file = st.file_uploader(
        "Upload a question paper (PDF or Image)",
        type=["pdf", "png", "jpg", "jpeg"]
    )

    if (st.session_state.get('qa_pairs') or st.session_state.get('similar_qa_pairs')):
        if st.button("Export Q&A to PDF"):
            export_to_pdf("exported_qa.pdf", st.session_state.qa_pairs, st.session_state.similar_qa_pairs)
            with open("exported_qa.pdf", "rb") as f:
                st.download_button("Download PDF", f, file_name="QnA_Export.pdf")

# Use session state to hold the uploaded file
# Initialize session state variables
if 'uploaded_file' not in st.session_state:
    st.session_state.uploaded_file = None
if 'qa_pairs' not in st.session_state:
    st.session_state.qa_pairs = []
if 'similar_qa_pairs' not in st.session_state:
    st.session_state.similar_qa_pairs = []

uploaded_file = st.session_state.uploaded_file

if uploaded_file:
    try:
        file_type = uploaded_file.type
        temp_file_path = "temp.pdf" if "pdf" in file_type else "temp.png"

        with open(temp_file_path, "wb") as f:
            f.write(uploaded_file.read())

        # OCR / Text extraction
        raw_text = extract_text_from_pdf(temp_file_path) if temp_file_path.endswith(".pdf") \
            else extract_text_from_image(temp_file_path)

        # Clean and parse into questions
        cleaned = clean_text(raw_text)
        questions = split_into_questions(cleaned)

        if questions:
            st.success(f"Extracted {len(questions)} question(s)")
        else:
            st.warning("No questions detected. Check document quality.")

        for i, q in enumerate(questions):
            if not q.strip():
                continue

            with st.expander(f"Question {i+1}", expanded=True):
                st.markdown(f"> {q.strip()}")

                # Actions: Hint, Answer, Similar Q
                col1, col2, col3 = st.columns(3)
                with col1:
                    if st.button(f"Hint", key=f"hint_{i}"):
                        try:
                            hint = get_hints(q)
                            st.info(hint)
                            audio_file = text_to_speech_file(hint)
                            st.audio(audio_file)
                        except Exception as e:
                            st.error(f"Error getting hints: {e}")
                with col2:
                    if st.button(f"Answer", key=f"ans_{i}"):
                        try:
                            answer = get_answer(q)
                            st.success(answer)
                            st.session_state.qa_pairs.append((q, answer))
                            audio_file = text_to_speech_file(answer)
                            st.audio(audio_file)
                        except Exception as e:
                            st.error(f"Error getting answer: {e}")
                with col3:
                    if st.button(f"Similar Q", key=f"sim_{i}"):
                        try:
                            alt_q = generate_similar_question(q)
                            st.warning(alt_q)
                            answer = get_answer(alt_q)
                            st.success(answer)
                            st.session_state.similar_qa_pairs.append((alt_q, answer))
                            audio_file = text_to_speech_file(answer)
                            st.audio(audio_file)
                        except Exception as e:
                            st.error(f"Error generating similar question: {e}")
                st.markdown("---")

    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
