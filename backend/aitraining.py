import spacy
from spacy.util import minibatch, compounding
from spacy.training import Example
from trainingdata import TRAINING_DATA


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


nlp = train_ner_model(TRAINING_DATA)

nlp.to_disk("./food_ner_model")
