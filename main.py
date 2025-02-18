import streamlit as st
import openai
import fitz  # PyMuPDF for PDF processing
import os

# Set your OpenAI API Key (Replace with your own key or use an environment variable)
openai_client = openai.Client(api_key="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  ")

def chat_with_gpt(prompt):
    """Function to interact with OpenAI GPT model"""
    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a helpful research assistant."},
                  {"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def extract_text_from_pdf(pdf_file):
    """Extract text from uploaded PDF file"""
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = "".join(page.get_text() for page in doc)
    return text[:2000]  # Limit text size to avoid token overflow

# Streamlit UI
st.title("📚 AI Research Assistant Chatbot")
st.write("Ask research-related queries or upload a PDF for summarization.")

# User input for chatbot
user_input = st.text_input("Ask your research question:")
if user_input:
    response = chat_with_gpt(user_input)
    st.write("### 🤖 Chatbot Response:")
    st.write(response)

# File uploader for PDF summarization
uploaded_file = st.file_uploader("Upload a research paper (PDF) for summarization:", type=["pdf"])
if uploaded_file:
    extracted_text = extract_text_from_pdf(uploaded_file)
    summary_prompt = f"Summarize the following research paper content:\n{extracted_text}"
    summary = chat_with_gpt(summary_prompt)
    st.write("### 📄 Summary:")
    st.write(summary)

# Footer
st.markdown("---")
st.write("🚀 Built with Streamlit by Sami")
