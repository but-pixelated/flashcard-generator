# Offline Flashcard Generator using Phi-3 (Ollama)

This is a fully offline Flashcard Generator powered by [Phi-3](https://ollama.com/library/phi3) using the [Ollama](https://ollama.com) runtime. It lets you:

-  Input **text** or **upload PDFs**
-  Generate flashcards in **Q/A format** using **phi3**
-  Export to **CSV** or directly as **.apkg (Anki Deck)**
-  No API keys, no internet needed — all runs locally on your system

---

## Features

- Text or PDF-based input  
- Use local LLM (**phi3**) via Ollama  
- Export to `.csv` for spreadsheets or `.apkg` for Anki  
- Option to choose how many flashcards to generate  
- Simple web UI using Streamlit  

---

## Installation (Mac & Windows)

### Prerequisites

Make sure the following are installed:

- **Python 3.9+**  
- [Git](https://git-scm.com/downloads)  
- [Ollama](https://ollama.com) *(for running local phi3 model)*  

---

###  Step-by-Step Setup

####  1. Clone this repo

```bash
git clone git@github.com:but-pixelated/flashcard-generator.git
cd flashcard-generator
```

---

####  2. Set up virtual environment

**Mac/Linux:**

```bash
python3 -m venv virtualenv
source virtualenv/bin/activate
```

**Windows:**

```bash
python -m venv virtualenv
virtualenv\Scripts\activate
```

---

###  3. Install dependencies

```bash
pip install -r requirements.txt
```

**The `requirements.txt` includes:**

- streamlit  
- pymupdf  
- pandas  
- genanki  
- ollama  

---

###  4. Install Ollama & Phi-3

Follow the instructions here:  
https://ollama.com/download

Then run:

```bash
ollama pull phi3
```

This will download the phi3 model locally (~2GB+)

---

##  Run the App

```bash
python -m streamlit run app.py (recommended, so it does not run the global venv)
or
streamlit run app.py
```

Visit in browser:  
http://localhost:8501

---

##  Usage Instructions

1. Choose Input Mode: Text or PDF  
2. Enter content or upload a PDF  
3. Choose number of flashcards to generate  
4. Click ** Generate Flashcards**  
5. View them in the app  
6. Download:
   -  as `.csv`  
   -  or as Anki `.apkg`  

---

##  Example Flashcard Format

```
Q: What is the powerhouse of the cell?  
A: The mitochondria, which generates energy (ATP) through cellular respiration.
```

---

##  Export Options

- **CSV**: Opens in Excel/Google Sheets  
- **Anki .apkg**: Importable directly into the Anki app  

---

##  Troubleshooting

-  No flashcards found?  
  → Try reducing input size or making input clearer  

-  App feels slow?  
  → Phi3 runs on CPU — be patient!  

-  Mac permission issues?  
  → Try `chmod +x` or allow Terminal access to documents  

---

##  File Structure

```
flashcard-generator/
├── app.py                 # main Streamlit app  
├── requirements.txt       # python3 dependencies  
├── README.md              # this file  
├── virtualenv/            # your Python env (not tracked in git)  
```

---

##  License

MIT License – free to use, fork, and improve.

---

##  Credits

Made with 💙 by [@but-pixelated](https://github.com/but-pixelated)  
Powered by:

- OpenAI’s Phi-3  
- Ollama  
- Streamlit  
- genanki
