# importing the requests library
import requests
import config
# api-endpoint
URL = config.cloud_function

r = requests.get(url = 'https://europe-west1-peaceful-basis-312016.cloudfunctions.net/API-Request')
r.status_code
r.headers['Content-Type']


data = r.json()




