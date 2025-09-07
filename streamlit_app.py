# streamlit_app.py
import streamlit as st
import spacy
from spacy import displacy
import pandas as pd

@st.cache_resource
def load_model():
    return spacy.load("en_core_web_sm")

nlp = load_model()

st.title("NER Demo — spaCy + Streamlit")
st.write("Enter any text and click Analyze to see Named Entities (PERSON, ORG, GPE, etc.).")

text = st.text_area("Input text", value="Elon Musk founded SpaceX and lives in Texas.")

if st.button("Analyze"):
    doc = nlp(text)
    # Render entities as HTML using displacy
    html = displacy.render(doc, style="ent", jupyter=False)
    st.components.v1.html(html, height=200, scrolling=True)

    # Prepare table
    rows = [{"text": ent.text, "label": ent.label_, "start": ent.start_char, "end": ent.end_char} for ent in doc.ents]
    if rows:
        df = pd.DataFrame(rows)
        st.dataframe(df)
        csv_bytes = df.to_csv(index=False).encode("utf-8")
        st.download_button("Download CSV", data=csv_bytes, file_name="entities.csv", mime="text/csv")
    else:
        st.info("No entities found.")
