# ner_demo.py
import spacy
import csv
from pathlib import Path

# Load spaCy model (make sure en_core_web_sm is downloaded)
nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    doc = nlp(text)
    entities = []
    for ent in doc.ents:
        entities.append({
            "text": ent.text,
            "label": ent.label_,
            "start_char": ent.start_char,
            "end_char": ent.end_char
        })
    return entities

def print_entities(entities):
    if not entities:
        print("No entities found.")
        return
    print(f"{'Entity':30} {'Label':10} {'Start':5} {'End':5}")
    print("-"*60)
    for e in entities:
        print(f"{e['text'][:30]:30} {e['label']:10} {e['start_char']:5} {e['end_char']:5}")

def save_entities_csv(entities, out_path="entities.csv"):
    p = Path(out_path)
    with p.open("w", newline="", encoding="utf8") as f:
        writer = csv.DictWriter(f, fieldnames=["text","label","start_char","end_char"])
        writer.writeheader()
        for ent in entities:
            writer.writerow(ent)
    print(f"Saved {len(entities)} entities to {out_path}")

if __name__ == "__main__":
    sample_text = (
        "Apple is looking to buy a startup in the United States. "
        "Elon Musk founded SpaceX and lives in Texas. "
        "Barack Obama visited New Delhi in 2019."
    )

    print("Input text:")
    print(sample_text)
    print("\n---\nExtracting entities...\n")

    entities = extract_entities(sample_text)
    print_entities(entities)

    # Save CSV
    save_entities_csv(entities, "entities.csv")
