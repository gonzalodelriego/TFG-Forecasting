import requests
import config
import json

def api_request ():
    response = requests.get(
      config.api_endpoint,
      # Las coordenadas corresponden a las de la boya de Santander
      params={
        'lat': config.lat,
        'lng': config.lng,
        'params': config.params,
      },
      headers={
        'Authorization': config.api_key
      }
    )
    
    # Do something with response data.
    json_data = response.json()
    return json_data

def save_json(json_data):
    with open("history.json", "w") as outfile: 
        json.dump(json_data, outfile, indent =7)
    
save_json(api_request())