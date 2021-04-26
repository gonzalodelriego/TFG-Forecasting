import requests
import config
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