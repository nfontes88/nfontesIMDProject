import requests  # to make API calls
import json  # to process the received data
import secrets
from numpy import arange


def main():
    url = "https://imdb-api.com/api#Top250TVs-header"
    api_key = "k_vn1z1026"
    results = requests.request("Get", url)
    print(results)
    results = json.result("Get", api_key)
    print(results)


def ratings_data():
    url = f"https://imdb-api.com/api#UserRatings-header/{1, 50, 100, 200}" + secrets.token_urlsafe()
    results = requests.request("Get", url)
    print(results)


def json_file():
    json_file = open('jsonData.json')
    data = json.load(json_file)
    print(data)
    json_file.close()


def save_file():
    user_rating = arange(1, 50, 100, 200)
    top_250tvs = arange()


with open("output_data.csv", "w") as out_file:
    for i in range(len(user_rating)):
        out_string = ""
        out_string += str(user_rating[i])
        out_string += str
        out_string = "," + (top_250tvs[i])
        out_string += "\n"
        out_file.write(out_string)







