from dotenv import load_dotenv
import os
import requests


load_dotenv()

client_id = os.getenv("API_KEY")
client_secret = os.getenv("API_SECRET")
access_token = ""

print("API_KEY: ", client_id)
print("API_SECRET: ", client_secret)


def getAuthToken():
    data = {
    'grant_type': 'client_credentials',
    'client_id': 'client_id',
    'client_secret': 'client_secret',
    }

    response = requests.post('https://accounts.spotify.com/api/token', data=data)

    return response


print(getAuthToken())
