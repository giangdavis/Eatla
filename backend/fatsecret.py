import requests
from requests_oauthlib import OAuth1
import os

consumer_key = os.environ["CONSUMER_KEY"]
consumer_secret = os.environ["CONSUMER_SECRET"]
access_token = os.environ["ACCESS_TOKEN"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]

def create_food_entry(food_entry_data):

    oauth = OAuth1(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret
    )

    url = 'https://platform.fatsecret.com/rest/server.api'
    params = {
        'method': 'food_entry.create',
        'format': 'json',
        **food_entry_data,
    }

    response = requests.post(url, params=params, auth=oauth)
    response_data = response.json()

    if 'error' in response_data:
        raise Exception(f"Error creating food entry: {response_data['error']}")

    food_entry_id = response_data['food_entry_id']['value']
    return food_entry_id
