from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")

print("API_KEY: ", api_key)
print("API_SECRET: ", api_secret)
