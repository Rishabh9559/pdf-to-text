import streamlit as st
import fitz  # PyMuPDF

def pdf_to_text(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    return full_text

# Streamlit UI
st.set_page_config(page_title="PDF to Text Converter", layout="centered")
st.title("📄 PDF to Text Converter")

uploaded_pdf = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_pdf is not None:
    with st.spinner("Processing... Please wait ⏳"):
        extracted_text = pdf_to_text(uploaded_pdf)

    st.success("✅ PDF converted to text!")

    # Display preview (optional)
    st.subheader("🔍 Text Preview")
    st.text_area("Extracted Text", extracted_text[:1000], height=200)

    # Download as .txt
    st.download_button(
        label="📥 Download as .txt",
        data=extracted_text,
        file_name="extracted_text.txt",
        mime="text/plain"
    )
