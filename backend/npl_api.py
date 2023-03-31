# nlp_api.py
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_food_information(text):
    doc = nlp(text)
    food_items = []
    quantities = []
    for token in doc:
        if token.ent_type_ == "PRODUCT":
            food_items.append(token.text)
        if token.ent_type_ == "QUANTITY":
            quantities.append(token.text)
    # TODO: Extract time of day and other relevant information
    return food_items, quantities
