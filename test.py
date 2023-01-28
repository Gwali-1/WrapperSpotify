from SportifyClient.sportifyclient import Client
import os
from dotenv import load_dotenv,dotenv_values
import datetime
import pytest


load_dotenv()


def test_get_auth_token_wit_wrong_credentials():
    credentials = {"ClientID":"wrong","ClientSecret":"wrong"}
    sportify = Client(credentials)
    response = sportify.get_auth_token()
    assert "error" in response,"should return an object with error description"
 

def test_get_auth_token_wit_right_credentials():
    credentials = {"ClientID":os.getenv("ClientID"),"ClientSecret":os.getenv("ClientSecret")}
    sportify = Client(credentials)
    response = sportify.get_auth_token()
    assert response is None

 

test_get_auth_token_wit_right_credentials()

def test_token_expired_with_expire_time_in_future():
    credentials = {"ClientID":os.getenv("ClientID"),"ClientSecret":os.getenv("ClientSecret")}
    sportify = Client(credentials)
    future_expire_time = datetime.datetime.now() + datetime.timedelta(hours=1)
    sportify.expire_time = future_expire_time
    value = sportify.token_expired()
    assert value == False 


def test_token_expired_with_expire_time_in_past():
    credentials = {"ClientID":os.getenv("ClientID"),"ClientSecret":os.getenv("ClientSecret")}
    sportify = Client(credentials)
    future_expire_time = datetime.datetime.now() - datetime.timedelta(hours=1)
    sportify.expire_time = future_expire_time
    value = sportify.token_expired()
    assert value == True 




def test_track_search_with_no_search_query():
    credentials = {"ClientID":os.getenv("ClientID"),"ClientSecret":os.getenv("ClientSecret")}
    sportify = Client(credentials)
    results = sportify.track_search("")
    assert "No search query" in results["error"]["message"]

def test_track_search_with_track_search_query():
    credentials = {"ClientID":os.getenv("ClientID"),"ClientSecret":os.getenv("ClientSecret")}
    sportify = Client(credentials)
    results = sportify.track_search("good morning")
    assert "name" in results[0]

def test_track_search_with_wrong_credentials():
    credentials = {"ClientID":"wrong","ClientSecret":"wrong"}
    sportify = Client(credentials)
    results = sportify.track_search("good morning")
    assert "Invalid access token" in  results["error"]["message"]



def test_artist_search_with_no_search_query():
    credentials = {"ClientID":os.getenv("ClientID"),"ClientSecret":os.getenv("ClientSecret")}
    sportify = Client(credentials)
    results = sportify.artist_search("")
    assert "No search query" in results["error"]["message"]



def test_artist_search_with_artist_search_query():
    credentials = {"ClientID":os.getenv("ClientID"),"ClientSecret":os.getenv("ClientSecret")}
    sportify = Client(credentials)
    results = sportify.artist_search("kanye west")
    assert "name" in results[0]
    


def test_artist_search_with_wrong_credentials():
    credentials = {"ClientID":"wrong","ClientSecret":"wrong"}
    sportify = Client(credentials)
    results = sportify.artist_search("kanye west")
    assert "Invalid access token" in  results["error"]["message"]


def test_get_related_artists_with_invalid_artist_id():
    credentials = {"ClientID":os.getenv("ClientID"),"ClientSecret":os.getenv("ClientSecret")}
    sportify = Client(credentials)
    results = sportify.get_related_artists("kanye west")
    assert "invalid id" in  results["error"]["message"]
    




def test_get_related_artists_with_valid_artist_id():
    credentials = {"ClientID":os.getenv("ClientID"),"ClientSecret":os.getenv("ClientSecret")}
    sportify = Client(credentials)
    results = sportify.get_related_artists("5K4W6rqBFWDnAN6FQUkS6x")
    assert "artists" in results
    




def test_get_avilable_genres_with_wrong_credentials():
    credentials = {"ClientID":"wrong","ClientSecret":"wrong"}
    sportify = Client(credentials)
    results = sportify.get_avilable_genres()
    assert "error" in results
    assert "Invalid access token" in  results["error"]["message"]


def test_get_avilable_genres_with_valid_credentials():
    credentials = {"ClientID":os.getenv("ClientID"),"ClientSecret":os.getenv("ClientSecret")}
    sportify = Client(credentials)
    results = sportify.get_avilable_genres()
    assert "genres" in results




# test_get_avilable_genres_with_valid_credentials()


def test_get_recommendations_with_missing_required_params():
    credentials = {"ClientID":os.getenv("ClientID"),"ClientSecret":os.getenv("ClientSecret")}
    sportify = Client(credentials)
    options =  {
        "seed_artists":"5K4W6rqBFWDnAN6FQUkS6x",
        "seed_genres":"alt-rock",
    }
    
    with pytest.raises(Exception) as error:
        sportify.get_recommendations(options)
        assert "missing required key" in str(error.value)



def test_get_recommendations_with_wrong_required_params():
    credentials = {"ClientID":os.getenv("ClientID"),"ClientSecret":os.getenv("ClientSecret")}
    sportify = Client(credentials)
    options =  {
        "seed_artists":"5K4W6rqBFWDnAN6FQUkS6x",
        "seed_genres":"alt-rock",
        "seed_tracks":"2wekjwd,"

    }

    results= sportify.get_recommendations(options)
    assert "error" in results
    assert "invalid request" in  results["error"]["message"]





def test_get_recommendations_with_correct_params():
    credentials = {"ClientID":os.getenv("ClientID"),"ClientSecret":os.getenv("ClientSecret")}
    sportify = Client(credentials)
    options =  {
        "seed_artists":"5K4W6rqBFWDnAN6FQUkS6x",
        "seed_genres":"alt-rock",
        "seed_tracks":"6MXXY2eiWkpDCezVCc0cMH,"

    }

    results= sportify.get_recommendations(options)
    assert "tracks" in results
    


