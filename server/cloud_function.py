# importing the requests library
import requests
import config
# api-endpoint
URL = config.cloud_function

r = requests.get(url = URL)
r.status_code
r.headers['Content-Type']


data = r.json()




