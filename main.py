import os
from dotenv import load_dotenv
from steam import webapi

load_dotenv()
api_key = os.getenv("API_KEY")

try:
    api = webapi.WebAPI(api_key)
    print("Connection to the Steam Web API was successfully established.")
except Exception as e:
    print(f"Error while calling the Steam Web API: {e}")
