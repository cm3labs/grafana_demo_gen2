from dotenv import load_dotenv
import os
import requests
from tools.auth import getAuthToken
from tools.json_prettify import json_prettify, replace_single_quotes_with_double_quotes

load_dotenv()

access_token = getAuthToken().get('access_token')
token_type = getAuthToken().get('token_type')

# # testing these vars ... these are good
# print(f"access_token: {access_token}")
# print(f"token_type: {token_type}")

# Our five artists in respective order: Jennifer Lopez, The Prodigy, Rhapsody of Fire, Lara Trump, Jamiroquai.
# I am losing time on the relevant aspect of this project, so I am going to cheat this part
artists = []


# get an artist as a json object
def getArtist(artist):
    headers = {
    'Authorization': f'{token_type} {access_token}',
    }

    response = requests.get(f'https://api.spotify.com/v1/artists/{artist}', headers=headers)

    artist_data = response.json()

    return artist_data

## testing a get of artist Children of Bodom
# (getArtist("1xUhNgw4eJDZfvumIpcz1B"))
# print(getArtist("1xUhNgw4eJDZfvumIpcz1B").get("name"))
# print(replace_single_quotes_with_double_quotes(json.dumps(getArtist("1xUhNgw4eJDZfvumIpcz1B"))))
print(json_prettify(getArtist("1xUhNgw4eJDZfvumIpcz1B")))