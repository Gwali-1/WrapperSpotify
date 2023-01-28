

# WrapperSpotify
This is light weight python wrapper for the spotify api. Ligh weight as it doesn't currently expose methods for all the
endpoint functionality provided by sportify, just a few. This wrapper client uses the client credential workflow hence does not expose 
methods for any fuctionality that require user scope or authorization(yet).

## Features
- [x] Handles token generation for you
- [x] Automatically refreshes tokens if they expire
- [x] Exposes methods to allow you to query the sportify api easily




## Usage

- Install with pip
```bash
pip install WrapperSpotify
```



## search for artist 
- create a dictionary with client credentials
- initialize client object 
- call method with `artist name`
```bash
    import WrapperSpotify 
    credentials = {
        "ClientID":os.getenv("ClientID"),
        "ClientSecret":os.getenv("ClientSecret")
    }

    client = WrapperSpotify.Client(credentials)
    results = client.artist_search("artist name")
    
```


The artist_search method takes some optional arguments
- `filter`
set to true by default. filters out  the results returned from api inti a smaller size. providing only some info such as 
artist id, profile , images etch
when set to false , results is not filtered and giant results from api is returned to you

>results = client.artist_search("artist name", filter=False)

- `limit`
set to 1 by default so results for only one artist is returned. You can increase range of results returned by increasing it .
check [spotify api docs ](https://developer.spotify.com/documentation/web-api/reference/#/operations/search) for detailed explanation
>results = client.artist_search("artist name", Limit=5)
will return results for 5 differents artist which matches your artist name argument








## search for track 
- create a dictionary with client credentials
- initialize client object 
- call method with `track name`
```bash
import WrapperSpotify
credentials = {
        "ClientID":os.getenv("ClientID"),
        "ClientSecret":os.getenv("ClientSecret")
    }

    client = WrapperSpotify.Client(credentials)
    results = client.track_search("track name")
    
```
The track_search method takes some optional arguments
- `filter`
set to true by default. filters out  the results returned from api inti a smaller size. providing only some info such as 
artist id, profile , images etch
when set to false , results is not filtered and giant results from api is returned to you

>results = client.artist_search("artist name", filter=False)


- `limit`
set to 1 by default so results for only one artist is returned. You can increase range of results returned by increasing it .
check [spotify api docs ](https://developer.spotify.com/documentation/web-api/reference/#/operations/search) for detailed explanation
>results = client.artist_search("artist name", Limit=5)










## search for related artist 
- create a dictionary with client credentials
- initialize client object 
- call method with `artist id`
```bash
    import WrapperSpotify
    credentials = {
        "ClientID":os.getenv("ClientID"),
        "ClientSecret":os.getenv("ClientSecret")
    }

    client = WrapperSpotify.Client(credentials)
    results = client.get_related_artists("artist id")
    
```
check [api docs ](https://developer.spotify.com/documentation/web-api/reference/#/operations/get-an-artists-related-artists) for detailed explanation








## search for track recommendations
- create a dictionary with client credentials
- initialize client object 
- call method with `dictionary containing query parameter keys and their values`
```bash
    import WrapperSpotify
    credentials = {
        "ClientID":os.getenv("ClientID"),
        "ClientSecret":os.getenv("ClientSecret")
    }

    client = WrapperSpotify.Client(credentials)

    options =  {
        "seed_artists":"5K4W6rqBFWDnAN6FQUkS6x",
        "seed_genres":"alt-rock",
        "seed_tracks":"6MXXY2eiWkpDCezVCc0cMH,"

    }

    results = client.get_recommendations(options)
    
```

 `seed_artists`,`seed_genres` and `seed_tracks` are required parameters for this endpoint and have to be added or an exception will be thrown.
    you can specify other parameters to filter recommendations by . check [api docs ](https://developer.spotify.com/documentation/web-api/reference/#/operations/get-recommendations)






## search for available genres 
- create a dictionary with client credentials
- initialize client object 
```bash
    import WrapperSpotify
    credentials = {
        "ClientID":os.getenv("ClientID"),
        "ClientSecret":os.getenv("ClientSecret")
    }

    client = WrapperSpotify.Client(credentials)
    results = client.get_avilable_genres()
    
```
check [api docs ](https://developer.spotify.com/documentation/web-api/reference/#/operations/get-recommendation-genres) for detailed explanation








