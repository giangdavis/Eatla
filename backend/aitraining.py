import spacy
from spacy.util import minibatch, compounding
from spacy.training import Example

TRAIN_DATA = [
    ("I had 1 serving of pizza for dinner.", {
        "entities": [(9, 10, "NUMBER_OF_UNITS"), (19, 24, "FOOD_NAME"), (29, 35, "MEAL")]
    }),
    ("2 servings of pasta for lunch today.", {
        "entities": [(0, 1, "NUMBER_OF_UNITS"), (12, 17, "FOOD_NAME"), (22, 27, "MEAL")]
    }),
        ("I had 2 slices of pizza for dinner.", {"entities": [(7, 8, "num_of_units"), (15, 20, "food_name"), (24, 30, "meal")]}),
    ("3 tacos for lunch", {"entities": [(0, 1, "num_of_units"), (2, 7, "food_name"), (11, 16, "meal")]}),
    # Add more examples
    # Add more training examples here
] 

def train_ner_model(training_data, n_iter=20):
    nlp = spacy.blank("en")
    ner = nlp.add_pipe("ner")

    for _, annotations in training_data:
        for ent in annotations.get("entities"):
            ner.add_label(ent[2])

    optimizer = nlp.initialize()

    for itn in range(n_iter):
        for raw_text, entity_offsets in training_data:
            doc = nlp.make_doc(raw_text)
            example = Example.from_dict(doc, {"entities": entity_offsets["entities"]})
            nlp.update([example], sgd=optimizer)

    return nlp

nlp = train_ner_model(training_data)

nlp.to_disk("./food_ner_model")

# custom_nlp = spacy.load("./custom_ner_model")
# text = "I had 3 servings of salad for lunch."
# doc = custom_nlp(text)

# food_name = None
# meal = None
# number_of_units = None

# for ent in doc.ents:
#     if ent.label_ == "FOOD_NAME":
#         food_name = ent.text
#     elif ent.label_ == "MEAL":
#         meal = ent.text
#     elif ent.label_ == "NUMBER_OF_UNITS":
#         number_of_units = float(ent.text)

# print("Food name:", food_name)
# print("Meal:", meal)
# print("Number of units:", number_of_units)
