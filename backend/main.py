from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from requests_oauthlib import OAuth1Session
import os
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

CONSUMER_KEY = os.environ["CONSUMER_KEY"]
CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]

app = FastAPI()

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

class AccessTokenData(BaseModel):
    oauth_token: str
    oauth_verifier: str

@app.get('/oauth/start') # DEBUG 
async def start_oauth():
    request_token_url = 'https://www.fatsecret.com/oauth/request_token'
    oauth = OAuth1Session(CONSUMER_KEY, client_secret=CONSUMER_SECRET)
    response = oauth.fetch_request_token(request_token_url)
    print(response)
    resource_owner_key = response.get('oauth_token')
    resource_owner_secret = response.get('oauth_token_secret')

    # Store resource_owner_key and resource_owner_secret securely

    authorization_url = oauth.authorization_url('https://www.fatsecret.com/oauth/authorize')
    return {'authorization_url': authorization_url}

@app.post('/create_food_entry')
def create_food_entry_route(food_entry_data: FoodEntryData):
    # Replace this with your actual implementation
    food_entry_id = food_entry_data.food_id
    return {'food_entry_id': food_entry_id}

@app.post('/oauth/access_token')
async def get_access_token(access_token_data: AccessTokenData):
    access_token_url = 'https://www.fatsecret.com/oauth/access_token'
    
    # Retrieve the resource_owner_secret associated with the oauth_token
    # You should have saved it in step 2
    resource_owner_secret = 'your_stored_resource_owner_secret'

    oauth = OAuth1Session(CONSUMER_KEY,
                          client_secret=CONSUMER_SECRET,
                          resource_owner_key=access_token_data.oauth_token,
                          resource_owner_secret=resource_owner_secret,
                          verifier=access_token_data.oauth_verifier)
    response = oauth.fetch_access_token(access_token_url)

    access_token = response.get('oauth_token')
    access_token_secret = response.get('oauth_token_secret')

    # Store access_token and access_token_secret securely

    return {'access_token': access_token, 'access_token_secret': access_token_secret}
