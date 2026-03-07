from transformers import pipeline

ner_model = pipeline(
    "ner",
    model="dslim/bert-base-NER",
    grouped_entities=True
)


def extract_entities(text):

    results = ner_model(text)

    entities = []

    for r in results:
        entities.append(r["word"])

    return entities