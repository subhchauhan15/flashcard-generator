# 🧠 Flashcard Generator using LLM (Ollama + Phi-3 + Streamlit)

This is a lightweight Flashcard Generator tool that uses the **Phi-3 Mini** language model locally (via [Ollama](https://ollama.com)) to convert educational content (text or PDFs) into concise **Q&A flashcards**. The interface is built using **Streamlit** for easy interaction and CSV export.

---

## 📌 Features

- ✅ Accepts **text input** or **PDF file upload**
- ✅ Uses **local LLM (Phi-3 Mini)** — no internet/API key required
- ✅ Generates **10 well-structured flashcards**
- ✅ Export flashcards to `.csv` format
- ✅ Subject input to improve relevance
- 🔒 Fully offline & privacy-safe

---

## 📂 Folder Structure
flashcard-generator/
├── app.py # Streamlit interface
├── llm_utils.py # Interaction with Ollama model
├── parser.py # PDF text extraction
├── flashcard_formatter.py # Prompt construction logic
├── requirements.txt # Dependencies
└── README.md


---

## 🚀 Getting Started

### 1. Install Ollama and Pull Model

Install Ollama from: [https://ollama.com](https://ollama.com)

Then pull the Phi-3 model:

```bash
ollama pull phi3:mini

=======
# flashcard-generator
Flashcard Generator using Ollama and Streamlit
>>>>>>> fe48bc66dc54bd0c2cda7beaefb8d5ec7029f020
