import spacy

custom_nlp = spacy.load("./food_ner_model")
text = "I had 3 servings of salad for lunch."
doc = custom_nlp(text)
print("Entities in '%s'" % text)

for ent in doc.ents:
    print(ent.label_, ent.text)

food_name = None
meal = None
number_of_units = None

for ent in doc.ents:
    if ent.label_ == "food_name":
        food_name = ent.text
    elif ent.label_ == "meal":
        meal = ent.text
    elif ent.label_ == "num_of_units":
        number_of_units = float(ent.text)

print("Food name:", food_name)
print("Meal:", meal)
print("Number of units:", number_of_units)
