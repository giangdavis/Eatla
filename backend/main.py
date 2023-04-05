from fastapi import FastAPI
from dotenv import load_dotenv
import os
from fastapi.middleware.cors import CORSMiddleware
from fatsecret import Fatsecret 
from pydantic import BaseModel
import spacy
from datetime import datetime


load_dotenv()

CONSUMER_KEY = os.environ["CONSUMER_KEY"]
CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]

app = FastAPI()
fs = Fatsecret(CONSUMER_KEY, CONSUMER_SECRET)
nlp = spacy.load("en_core_web_sm")

origins = [
    "http://localhost",
    "http://localhost:8000",
    "exp://",
    "*",
    "192.168.165.184:19000" # Replace with your local IP address
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class FoodEntryData(BaseModel):
    food_id: int
    food_entry_name: str
    serving_id: int
    number_of_units: float
    meal: str

def parse_food_entry(text):
    doc = nlp(text)
    food_id = None
    food_entry_name = None
    serving_id = None
    number_of_units = None
    meal = None

    # Extract food information from the text
    for token in doc:
        # You can customize the conditions to extract the information you need
        if token.ent_type_ == "PRODUCT":
            food_entry_name = token.text
        elif token.ent_type_ == "QUANTITY":
            number_of_units = float(token.text)
        # Add other conditions here to extract food_id, serving_id, and meal

    # Set default values if the information is not available
    food_id = food_id or "12345"  # Replace with a default food_id
    serving_id = serving_id or "67890"  # Replace with a default serving_id
    meal = meal or "other"

    return food_id, food_entry_name, serving_id, number_of_units, meal

@app.get('/auth')
async def get_auth_url():
    auth_url = fs.get_authorize_url() 
    return {'auth_url': auth_url}

@app.get('/authenticate/{pin}')
def authenticate_pin(pin: str):
    session_token = fs.authenticate(pin)
    return {'session_token': session_token}

@app.get('/profile/{session_token}')
def profile(session_token: str):
    new_session = Fatsecret(CONSUMER_KEY, CONSUMER_SECRET, session_token=session_token)
    food = new_session.foods_get_most_eaten()
    return {'food': food}

@app.post('/create_food_entry')
def create_food_entry_route(food_entry_data: FoodEntryData):
    text = parse_food_entry(str(food_entry_data))
    return {'text': text}


