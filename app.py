import streamlit as st
import pandas as pd
from parser import extract_text_from_pdf
from llm_utils import query_ollama
from flashcard_formatter import build_flashcard_prompt

st.title("📚 Flashcard Generator using Phi-3 (Ollama)")

input_method = st.radio("Choose input method:", ["Paste Text", "Upload PDF"])
subject = st.text_input("Subject (optional):")

raw_text = ""
if input_method == "Paste Text":
    raw_text = st.text_area("Enter your text here:")
elif input_method == "Upload PDF":
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
    if uploaded_file:
        raw_text = extract_text_from_pdf(uploaded_file)

if st.button("Generate Flashcards"):
    if raw_text:
        with st.spinner("Generating..."):
            prompt = build_flashcard_prompt(raw_text, subject)
            output = query_ollama(prompt)
            flashcards = output.strip().split("\n\n")

            # Parse flashcards into Q&A
            qa_pairs = []
            for card in flashcards:
                if "Q:" in card and "A:" in card:
                    q = card.split("Q:")[1].split("A:")[0].strip()
                    a = card.split("A:")[1].strip()
                    qa_pairs.append({"Question": q, "Answer": a})

            if qa_pairs:
                st.success("✅ Flashcards Generated!")
                for i, pair in enumerate(qa_pairs, 1):
                    st.markdown(f"### Flashcard {i}")
                    st.markdown(f"**Q:** {pair['Question']}")
                    st.markdown(f"**A:** {pair['Answer']}")

                # Convert to DataFrame and export
                df = pd.DataFrame(qa_pairs)
                csv = df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="📥 Download Flashcards as CSV",
                    data=csv,
                    file_name='flashcards.csv',
                    mime='text/csv',
                )
            else:
                st.error("⚠️ No flashcards found in model response.")
    else:
        st.warning("Please provide input text or upload a PDF.")
