import streamlit as st
import ollama
import fitz
import pandas as pd
import genanki
import random
import io
import re
def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text


def parse_flashcards(raw_text):
    flashcards = []
    matches = re.findall(r'Q\d*:\s*(.*?)\nA\d*:\s*(.*?)(?=\nQ\d*:|\Z)', raw_text, re.DOTALL)
    for q, a in matches:
        flashcards.append({
            "question": q.strip(),
            "answer": a.strip()
        })

    return flashcards
def export_to_anki(flashcards, deck_name="AI Flashcards"):
    my_deck = genanki.Deck(
        random.randint(1000000, 9999999),
        deck_name
    )
    my_model = genanki.Model(
        random.randint(1000000, 9999999),
        'Flashcard Model',
        fields=[
            {'name': 'Question'},
            {'name': 'Answer'}
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Question}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
            },
        ])
    for card in flashcards:
        note = genanki.Note(
            model=my_model,
            fields=[card["question"], card["answer"]]
        )
        my_deck.add_note(note)
    genanki.Package(my_deck).write_to_file("flashcards.apkg")

st.set_page_config(page_title=" Flashcard Generator (Offline)", layout="centered")

st.title(" Flashcard Generator with phi3 (Offline)")

input_mode = st.radio("Choose Input Mode", ["Text", "PDF"])

input_text = ""
if input_mode == "Text":
    input_text = st.text_area("Enter text to convert into flashcards")
elif input_mode == "PDF":
    uploaded_file = st.file_uploader("Upload your PDF", type="pdf")
    if uploaded_file:
        st.success("PDF uploaded successfully!")
        input_text = extract_text_from_pdf(uploaded_file)

num_flashcards = st.slider(" Number of flashcards to generate", 1, 50, 5)

if st.button(" Generate Flashcards"):
    if input_text.strip() == "":
        st.warning("Please enter some text or upload a PDF!")
    else:
        with st.spinner("Generating flashcards with phi3..."):
            response = ollama.chat(
                model='phi3',
                messages=[
                    {"role": "system", "content": "You are a flashcard generator. For the provided content, generate flashcards in Q&A format. Format each like:\nQ: ...\nA: ..."},
                    {"role": "user", "content": f"Generate exactly {num_flashcards} flashcards for the following text:\n\n{input_text[:3000]}"}
                ]
            )

            flashcards_raw = response['message']['content']
            st.code(flashcards_raw, language='markdown')
            flashcards = parse_flashcards(flashcards_raw)[:num_flashcards]

            if flashcards:
                st.subheader(" Flashcards")
                for i, fc in enumerate(flashcards):
                    with st.expander(f"Q{i+1}: {fc['question']}"):
                        st.markdown(f"**A:** {fc['answer']}")

                df = pd.DataFrame(flashcards)
                csv = df.to_csv(index=False)
                st.download_button(" Download as CSV", data=csv, file_name="flashcards.csv", mime="text/csv")

                if st.button(" Export to Anki"):
                    export_to_anki(flashcards)
                    with open("flashcards.apkg", "rb") as f:
                        st.download_button(" Download .apkg", data=f, file_name="flashcards.apkg")
            else:
                st.error("No flashcards could be parsed from the response.")
