import os
from datetime import datetime
from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from fatsecret import Fatsecret
from pydantic import BaseModel
import spacy

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
    "192.168.165.184:19000",  # Replace with your local IP address
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Data(BaseModel):
    user: str


class FoodEntryData(BaseModel):
    """
    Represents a food entry submitted by a user.

    Fields:
    - text: str - the text of the food entry
    """

    text: str


# i have two labels: meal and food_name
# i want to extract the meal and food_name from the text
# and then return the meal and food_name as a dictionary
def parse_food_entry(text):
    doc = nlp(text)

    food_name = None
    meal = None

    for ent in doc.ents:
        if ent.label_ == "food_name":
            food_name = ent.text
        elif ent.label_ == "meal":
            meal = ent.text

    return {"food_name": food_name, "meal": meal}


@app.get("/auth")
async def get_auth_url():
    auth_url = fs.get_authorize_url()
    return {"auth_url": auth_url}


@app.get("/authenticate/{pin}")
def authenticate_pin(pin: str):
    session_token = fs.authenticate(pin)
    return {"session_token": session_token}


@app.get("/profile/{session_token}")
def profile(session_token: str):
    new_session = Fatsecret(CONSUMER_KEY, CONSUMER_SECRET, session_token=session_token)
    food = new_session.foods_get_most_eaten()
    return {"food": food}


@app.post("/create_food_entry")
def create_food_entry(food_entry_data: FoodEntryData):
    return {"text": food_entry_data.text}
    # text = parse_food_entry(food_entry_data)
    # return {"text": text}


@app.get("/test_connection")
async def test_connection():
    return {"message": "connection successful"}
