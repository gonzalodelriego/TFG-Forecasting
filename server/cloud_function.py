# importing the requests library
import requests
import config
import pandas as pd
from sklearn.linear_model import LinearRegression

def get_data_from_api():
    response = requests.get(
      config.api_endpoint,
      params={
        'lat': config.lat,
        'lng': config.lng,
        'params': config.params
      },
      headers={
        'Authorization': config.api_key
      }
    )
    json_data = response.json()
    return json_data

def get_tide_from_api():
  response = requests.get(
  config.api_tide_endpoint,
  params={
    'lat': config.lat,
    'lng': config.lng  
  },
  headers={
    'Authorization': config.api_key
  }
  )
  json_data = response.json()
  return json_data

def set_data(data):
    data_list = []
    for x in data['hours']:
       aux_dict = {}
       aux_data_dict = {}
       aux_data_dict['swellDirection'] = [x['swellDirection']['meteo']]
       aux_data_dict['swellHeight'] = [x['swellHeight']['meteo']]
       aux_data_dict['swellPeriod'] = [x['swellPeriod']['meteo']]
       aux_data_dict['windSpeed'] = [x['windSpeed']['sg']]
       aux_data_dict['windDirection'] = [x['windDirection']['sg']]
       aux_data_dict['tide'] = [""]
       aux_data_dict['sardinero_uno'] = 0
       aux_data_dict['sardinero_dos'] = 0
       aux_data_dict['mataleñas'] = 0
       aux_data_dict['cañones'] = 0
       aux_data_dict['rosamunda'] = 0
       aux_data_dict['valdearenas'] = 0
       aux_data_dict['canallave'] = 0
       aux_data_dict['somo'] = 0
       aux_data_dict['langre'] = 0
       aux_data_dict['usgo'] = 0
       aux_data_dict['gerra'] = 0
       aux_data_dict['farolillo'] = 0
       aux_data_dict['brusco'] = 0
       aux_data_dict['santamarina'] = 0
       aux_data_dict['fortaleza'] = 0
       aux_data_dict['laredo'] = 0     
       aux_dict[x['time']] = aux_data_dict 
       data_list.append(aux_dict)
    return data_list

def set_tides(data,tides):
    for x in data:
        for date in x:
            ymd = date[0:10]
            for tide in tides['data']:
                fecha = tide['time']
                amd = fecha[0:10]
                if (ymd == amd):
                    hour = date[11:13]
                    hora = fecha[11:13]
                    minuto = fecha[14:16] 
                    redondeo = '0'+str(round(float(hora+"."+minuto)))
                    if(hour==redondeo):
                        x[date]['tide']=tide['type']
def calculate_tides(data):
    tides = data["tide"]
    counter = 0
    tide_counter = 0
    for tide in tides.values:
        if(tide =="high"):
            index = counter-tide_counter
            if (tide_counter == 3):
                tides.values[index] = "low"
                tides.values[index+1] = "medium-high"
                tides.values[index+2] = "high"
            if (tide_counter == 4):
                tides.values[index] = "low"
                tides.values[index+1] = "low"
                tides.values[index+2] = "medium-high"
                tides.values[index+3] = "high"
            if (tide_counter == 5):
                tides.values[index] = "low"
                tides.values[index+1] = "low"
                tides.values[index+2] = "medium-high"
                tides.values[index+3] = "high"
                tides.values[index+4] = "high"     
            if (tide_counter == 6):
                tides.values[index] = "low"
                tides.values[index+1] = "low"
                tides.values[index+2] = "medium-high"
                tides.values[index+3] = "medium-high"
                tides.values[index+4] = "high"
                tides.values[index+5] = "high"
            if (tide_counter == 7):
                tides.values[index] = "low"
                tides.values[index+1] = "low"
                tides.values[index+2] = "medium-high"
                tides.values[index+3] = "medium-high"
                tides.values[index+4] = "medium-high"
                tides.values[index+5] = "high"
                tides.values[index+6] = "high"
            if (tide_counter == 8):
                tides.values[index] = "low"
                tides.values[index+1] = "low"
                tides.values[index+2] = "medium-high"
                tides.values[index+3] = "medium-high"
                tides.values[index+4] = "medium-high"
                tides.values[index+5] = "medium-high"
                tides.values[index+6] = "high"
                tides.values[index+7] = "high"
            tide_counter = 0
            counter+=1
            continue
            
        if(tide == "low"):
            index = counter-tide_counter
            if (tide_counter == 3):
                tides.values[index] = "high"
                tides.values[index+1] = "medium-low"
                tides.values[index+2] = "low"
            if (tide_counter == 4):
                tides.values[index] = "high"
                tides.values[index+1] = "high"
                tides.values[index+2] = "medium-low"
                tides.values[index+3] = "low"
            if (tide_counter == 5):
                tides.values[index] = "high"
                tides.values[index+1] = "high"
                tides.values[index+2] = "medium-low"
                tides.values[index+3] = "low"
                tides.values[index+4] = "low"     
            if (tide_counter == 6):
                tides.values[index] = "high"
                tides.values[index+1] = "high"
                tides.values[index+2] = "medium-low"
                tides.values[index+3] = "medium-low"
                tides.values[index+4] = "low"
                tides.values[index+5] = "low"
            if (tide_counter == 7):
                tides.values[index] = "high"
                tides.values[index+1] = "high"
                tides.values[index+2] = "medium-low"
                tides.values[index+3] = "medium-low"
                tides.values[index+4] = "medium-low"
                tides.values[index+5] = "low"
                tides.values[index+6] = "low"
            if (tide_counter == 8):
                tides.values[index] = "high"
                tides.values[index+1] = "high"
                tides.values[index+2] = "medium-low"
                tides.values[index+3] = "medium-low"
                tides.values[index+4] = "medium-low"
                tides.values[index+5] = "medium-low"
                tides.values[index+6] = "low"
                tides.values[index+7] = "low"
            tide_counter = 0
            counter+=1
            continue
        
        counter+=1
        tide_counter+=1  
                     
def set_calification(data):
    spots = config.spots
    for x in data:
        new_data = {'swellDirection': x['swellDirection'],
            'swellHeight':data[x]['swellDirection'],
            'swellPeriod':data[x]['swellDirection'],
            'windSpeed':data[x]['swellDirection'],
            'windDirection':data[x]['swellDirection'],
            'tide':data[x]['swellDirection']
            }
        for spot in spots:
            calification = model(spot,new_data)
            data[x][spot] = calification

def model(spot,api_data):
    df = pd.read_csv (config.csv_calificated_history_path)
    x = df[['swellDirection','swellHeight','swellPeriod','windSpeed','windDirection','tide']]
    y = df[spot]
    regresion = LinearRegression()
    regresion.fit(x,y)
    prediccion = regresion.predict(api_data)
    
    # evaluacion = regresion.score(x_test, y_test)
    return prediccion
    
def cloud_function():
    data = get_data_from_api()
    aux_list = set_data(data)
    tides = get_tide_from_api()
    set_tides(aux_list,tides)
    # FALTAN DE CALCULAR TODAS LAS MAREAS
    calculate_tides(aux_list)
    set_calification(aux_list)
    return aux_list
# api-endpoint
# URL = config.cloud_function
# r = requests.get(url = URL)
# r.status_code
# r.headers['Content-Type']

res = cloud_function()
# data = r.json() 


