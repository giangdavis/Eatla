from requests_oauthlib import OAuth1Session
import os 
from dotenv import load_dotenv

# Replace these with your own FatSecret API credentials

# load dot env 

load_dotenv()

CONSUMER_KEY = os.environ["CONSUMER_KEY"]
CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]


# Step 1: Obtain a Request Token
request_token_url = 'https://oauth.fatsecret.com/connect/request_token'
oauth = OAuth1Session(CONSUMER_KEY, client_secret=CONSUMER_SECRET)
fetch_response = oauth.fetch_request_token(request_token_url)
resource_owner_key = fetch_response.get('oauth_token')
resource_owner_secret = fetch_response.get('oauth_token_secret')

# Step 2: Redirect the user to FatSecret's authorization URL
base_authorization_url = 'https://oauth.fatsecret.com/connect/authorize'
authorization_url = oauth.authorization_url(base_authorization_url)

print('Please go here and authorize:', authorization_url)

# Step 3: The user authorizes your application and is redirected back to your app
# Here, you should capture the oauth_verifier parameter from the redirected URL
oauth_verifier = input('Please input the oauth_verifier from the redirected URL: ')

# Step 4: Exchange the Request Token for an Access Token and Access Token Secret
access_token_url = 'https://oauth.fatsecret.com/connect/access_token'
oauth = OAuth1Session(CONSUMER_KEY,
                      client_secret=CONSUMER_SECRET,
                      resource_owner_key=resource_owner_key,
                      resource_owner_secret=resource_owner_secret,
                      verifier=oauth_verifier)
oauth_tokens = oauth.fetch_access_token(access_token_url)

access_token = oauth_tokens['oauth_token']
access_token_secret = oauth_tokens['oauth_token_secret']

print('Access Token:', access_token)
print('Access Token Secret:', access_token_secret)
