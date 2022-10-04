import requests
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

def search_api(search):
    url = os.environ.get("API_URL")

    querystring = {"q": search, "pageNumber": os.environ.get(
        "REQUEST_PAGENUMBER"), "pageSize": os.environ.get("REQUEST_PAGESIZE"), "autoCorrect": "true"}

    headers = {
        "X-RapidAPI-Key": os.environ.get("API_KEY"),
        "X-RapidAPI-Host": os.environ.get("API_HOST")
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.json()

# print(search_api('Tom Cruise'))
