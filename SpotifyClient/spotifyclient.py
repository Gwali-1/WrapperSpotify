import requests
from dotenv import load_dotenv
import os
import base64
import json
import datetime


load_dotenv()


class Client:
    """This is a class that defines methods and attributes used to establish a connection with sportify, generating authorization token
    and making request to specific endpoints 
    """


    def __init__(self, credentials):
        self.credentials = credentials
        if not isinstance(self.credentials,dict):
           raise Exception("Pass credientials as an object")

        self.__client_id = self.credentials["ClientID"]
        self.__client_secrete = self.credentials["ClientSecret"]
        self.expire_time = None
        self.__token= None
        

    

    def get_token_header(self):
        encoded_string = base64.b64encode(f"{self.__client_id}:{self.__client_secrete}".encode()).decode()
        return {"Authorization":f"Basic {encoded_string}", "Content-Type":"application/x-www-form-urlencoded"}


    def get_auth_header(self):
        if self.__token is  None or self.token_expired():
                self.get_auth_token()
                return {"Authorization":f"Bearer {self.__token}", "Content-Type":"application/json","Accept": "application/json"}
            
        return {"Authorization":f"Bearer {self.__token}", "Content-Type":"application/json","Accept": "application/json"}       


    def _get_expire_time(self,time):
        """ returns expire times for current token """
        return datetime.datetime.now() + datetime.timedelta(seconds=time)


    def get_auth_token(self):
        """ get new auth token """

        url = "https://accounts.spotify.com/api/token"
        header = self.get_token_header()
        body  = {"grant_type":"client_credentials"}
        response = requests.post(url,headers=header,data=body)
        if response.status_code in range(200,299):
            response_object = response.json()
            self.__token = response_object["access_token"]
            self.expire_time = self._get_expire_time(response_object["expires_in"])
            return None
        else:
            return response.json() 


    def token_expired(self):
        """ returns whether token is expired or not"""
        now = datetime.datetime.now()
        return self.expire_time < now


    def track_search_filter(self,data):
        results = []
        for item in data:
            track_info = {
                "images":item["album"]["images"],
                "name":item["name"],
                "preview_url":item["preview_url"],
                "artist_profile":item["artists"][0]["external_urls"]["spotify"],
                "popularity":item["popularity"],
                "track_id":item["id"]
            }
            results.append(track_info)

        return results


    def artist_search_filter(self,data):
        results = []
        for  item in data:
            artist_info = {
                "images":item["images"],
                "name":item["name"],
                " genres":item["genres"],
                "artist_profile":item["external_urls"]["spotify"],
                "popularity":item["popularity"],
                "artist_id":item["id"]

            }
            results.append(artist_info)

        return results

            


    #____________endpoint methods___________#


    def track_search(self,name,limit=1, filter=True):
        """search for artist tracks with name"""

        if self.__token is None or self.token_expired():
            self.get_auth_token()
            print("no token")
            
        url = "	https://api.spotify.com/v1/search"
        payload = {"q":name,"type":"track","limit":limit}
        headers= self.get_auth_header()
        response = requests.get(url, params=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()  #filter output for desired information
            if not filter: # if 
                return data
            return self.track_search_filter(data["tracks"]['items'])
        else:
            return response.json()




    def artist_search(self, name, limit=1,filter=True):
        """search for artist  with their  name"""

        if self.__token is None or self.token_expired():
            self.get_auth_token()
            print("no token")
            
        url = "	https://api.spotify.com/v1/search"
        payload = {"q":name,"type":"artist","limit":limit}
        headers= self.get_auth_header()
        response = requests.get(url, params=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()  #filter output for desired information
            if not filter: # if 
                return data
            return self.artist_search_filter(data["artists"]['items'])
        else:
            return response.json()

       

    def get_related_artists(self,artist_id):
        if self.__token is None or self.token_expired():
            self.get_auth_token()

        url =f"https://api.spotify.com/v1/artists/{artist_id}/related-artists"
        headers = self.get_auth_header()
        response = requests.get(url,headers=headers)
        data = response.json()
        return data




    def get_recommendations(self, options):
        """ returns a list of tracks based on seed information among others"""

        if self.__token is None or self.token_expired():
            self.get_auth_token()

        url = "https://api.spotify.com/v1/recommendations"

        required = ["seed_genres","seed_artists","seed_tracks"]
        for key in required:
            if key not in options.keys():
                raise Exception(f"missing required key, '{key}' ")
    
        headers = self.get_auth_header()
        response = requests.get(url,headers=headers,params=options)
        return response.json()





    def get_avilable_genres(self):
        """ returns a list of available genre names"""

        if self.__token is None or self.token_expired():
             self.get_auth_token()
        url = "https://api.spotify.com/v1/recommendations/available-genre-seeds"
        headers= {"Authorization":f"Bearer {self.__token}", "Content-Type":"application/json" , "Content-Type": "application/json"}
        response = requests.get(url, headers=headers)
        return response.json()



    # def __repr__(self):
    #     return "<Sportify connected client instance>"


        


