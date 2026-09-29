import PyPDF2
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY", "YOUR_GEMINI_API_KEY"))
model = genai.GenerativeModel('models/gemini-1.5-pro')

def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def ask_from_pdf(pdf_text: str, question: str):
    prompt = f"""
    Nee oru teacher. Keela irukka PDF content-a base panni kelvi-ku badhil sollu.
    
    PDF CONTENT:
    {pdf_text[:10000]}  # First 10000 chars mattum

    QUESTION: {question}
    """
    response = model.generate_content(prompt)
    return response.text
