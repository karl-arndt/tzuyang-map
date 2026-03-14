import requests
import time

def find_restaurant(address):
    # Implement logic to find restaurant based on address
    # This could involve calling an API like Google Maps or Yelp
    pass

def get_lat_lon(address):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": address,
        "format": "json",
        "limit": 1
    }
    
    headers = { "User-Agent": "tzuyang-map/1.0" }
    response = requests.get(url, params=params, headers=headers)
    data = response.json()
    if data:
        return float(data[0]['lat']), float(data[0]['lon'])
    else:
        return None, None