from mimetypes import init
import requests
import urllib.parse
import json

class MapBox:
    def __init__(self, access_token) -> None:
        self.root_url = "https://api.mapbox.com/geocoding/v5/mapbox.places/{}.json?types=place&access_token={}"
        self.access_token = access_token

    def getCoordinates(self, location_str):
        if location_str == "":
            return (0,0)
        formatted_location = urllib.parse.quote(location_str)
        url = self.root_url.format(formatted_location, self.access_token)
        response = requests.get(url)
        data = json.loads(response.text)
        if (len(data["features"]) > 0):
            coordinates = data["features"][0]["center"]
            if coordinates != None and len(coordinates) == 2:
                return (coordinates[1], coordinates[0])
        else:
            return (0,0)
        

mb = MapBox("pk.eyJ1IjoiYW5kcmV3aHVhbmciLCJhIjoiY2t5a3dzbDMxMWdrMTJ4b2wzMjlqNXZvNyJ9.K6nzS4XPLOfQ0srwV3M5rw")

# https://api.mapbox.com/geocoding/v5/mapbox.places/Collegeville%2C%20PA.json?access_token=pk.eyJ1IjoiYW5kcmV3aHVhbmciLCJhIjoiY2t5a3dyZWJvMzBrMTJxcG0xenBtYTdhZiJ9.uFJLIrcDl4OHJu1S-To2xA
# https://api.mapbox.com/geocoding/v5/mapbox.places/Collegeville%2C%20PA..hson?access_token=pk.eyJ1IjoiYW5kcmV3aHVhbmciLCJhIjoiY2t5a3dzbDMxMWdrMTJ4b2wzMjlqNXZvNyJ9.K6nzS4XPLOfQ0srwV3M5rw