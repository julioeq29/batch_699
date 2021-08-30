import geocoder
import os

def geocode(address):
    mapbox_api_key = os.getenv('MAPBOX_API_KEY')
    g = geocoder.mapbox(address, key=mapbox_api_key)
    return (g.json['lat'], g.json['lng'])
