from dotenv import load_dotenv
import os
import requests


load_dotenv()

client_id = os.getenv("API_KEY")
client_secret = os.getenv("API_SECRET")
access_token = ""


# # only for testing purposes
# print("API_KEY: ", client_id)
# print("API_SECRET: ", client_secret)


# takes your secrets, asks spotify for a token, gives you back array including access_token to be used in future requests"
def getAuthToken():
    data = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
    }

    response = requests.post('https://accounts.spotify.com/api/token', data=data)

    # converts results of getAuthToken() to .json file with these keys
    #       {'access_token': ,
    #       'token_type': , 
    #       'expires_in': }

    auth_token = response.json()

    return auth_token

