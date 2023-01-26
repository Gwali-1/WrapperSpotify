import requests
from dotenv import load_dotenv, dotenv_values
import os
import base64
import json
import datetime


load_dotenv()


now = datetime.datetime.now()
print(now)

future  = now + datetime.timedelta(seconds=60)
print(future)


class Client:

    credentials = None
    client_id=None
    client_secrete=None
    expire_time = None


    def __init__(self, credentials):
        self.credentials = credentials
        if not isinstance(self.credentials,dict):
           raise Exception("Pass credientials as an object")

        self.client_id = self.credentials["ClientID"]
        self.client_secrete = self.credentials["ClientSecret"]




        def get_auth_token(self):
            pass


        def check_token_expiry(self):
            pass

        def fetch_tracks(self):
            pass

        def fetch_playlist(self):
            pass

        


x = Client({"ClientID":os.getenv("ClientID"),"ClientSecret":os.getenv("ClientSecret")})


# config = dotenv_values(".env")




# def auth_string(id,secrete):
#     return base64.b64encode(f"{id}:{secrete}".encode()).decode()

# encode_string = auth_string(os.getenv("ClientID"),os.getenv("ClientSecret"))



# url = "https://accounts.spotify.com/api/token"
# body = {"grant_type":"client_credentials"}
# headers= {"Authorization":f"Basic {encode_string}", "Content-Type":"application/x-www-form-urlencoded"}

# response = requests.post(url, headers=headers,data=body)
# data = response.json()
# print(data)
# token = data.get("access_token")
# print(token)



# def get_generes(token):
#     url = "https://api.spotify.com/v1/recommendations/available-genre-seeds"
#     headers= {"Authorization":f"Bearer {token}", "Content-Type":"application/x-www-form-urlencoded"}
#     response = requests.post(url, headers=headers)
#     print(response.content)



# def search_artist(name):
#     url = "	https://api.spotify.com/v1/search"
#     payload = {"q":name,"type":"track","limit":"2"}
#     headers= {"Authorization":f"Bearer {token}", "Content-Type":"application/x-www-form-urlencoded"}
#     response = requests.get(url, params=payload, headers=headers)
#     data = response.json()
#     print(json.dumps(data, indent=2))
#     return data

# print("=====================")
# result = search_artist("moon")

# print(result["tracks"]["items"][0]["artists"][0]["name"])
