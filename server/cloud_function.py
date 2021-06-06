# importing the requests library
import requests
import config
import pandas as pd
import time
import json
import copy
import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import datetime


# Este método se encarga de recuperar de la API los datos meteorológicos necesarios para la calificación:
# SwellPeriod, SwellHeight, SwellDirection, WindSpeed, WindDirection, Time
# Extra: WaterTemperature
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

# Este método se encarga de recuperar los datos de la API correspondientes a la marea 
# Tide
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
       aux_data_dict['swellDirection'] = [x['swellDirection']['sg']]
       aux_data_dict['swellHeight'] = [x['swellHeight']['sg']]
       aux_data_dict['swellPeriod'] = [x['swellPeriod']['sg']]
       aux_data_dict['windSpeed'] = [x['windSpeed']['sg']]
       aux_data_dict['windDirection'] = [x['windDirection']['sg']]
       aux_data_dict['waterTemperature'] = [x['waterTemperature']['sg']]
       aux_data_dict['tide'] = [""]
       aux_data_dict['sardinero_uno'] = 0
       aux_data_dict['sardinero_dos'] = 0
       aux_data_dict['matalenias'] = 0
       aux_data_dict['caniones'] = 0
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
                    if (int(hora)<= 9):
                        redondeo = '0'+str(round(float(hora+"."+minuto)))
                    if (int(hora)>= 10):
                        redondeo = str(round(float(hora+"."+minuto)))
                    if(hour==redondeo):
                        x[date]['tide']=[tide['type']]
def calculate_tides(data):
    tides_list = []
    for element in data:
        date = list(element.keys())[0]
        tide = element[date]['tide'][0]
        tides_list.append(tide)
    counter = 0
    tide_counter = 0
    for tide in tides_list:
        if(tide =="high"):
            index = counter-tide_counter
            if (tide_counter == 3):
                tides_list[index] = "low"
                tides_list[index+1] = "medium-high"
                tides_list[index+2] = "high"
            if (tide_counter == 4):
                tides_list[index] = "low"
                tides_list[index+1] = "low"
                tides_list[index+2] = "medium-high"
                tides_list[index+3] = "high"
            if (tide_counter == 5):
                tides_list[index] = "low"
                tides_list[index+1] = "low"
                tides_list[index+2] = "medium-high"
                tides_list[index+3] = "high"
                tides_list[index+4] = "high"     
            if (tide_counter == 6):
                tides_list[index] = "low"
                tides_list[index+1] = "low"
                tides_list[index+2] = "medium-high"
                tides_list[index+3] = "medium-high"
                tides_list[index+4] = "high"
                tides_list[index+5] = "high"
            if (tide_counter == 7):
                tides_list[index] = "low"
                tides_list[index+1] = "low"
                tides_list[index+2] = "medium-high"
                tides_list[index+3] = "medium-high"
                tides_list[index+4] = "medium-high"
                tides_list[index+5] = "high"
                tides_list[index+6] = "high"
            if (tide_counter == 8):
                tides_list[index] = "low"
                tides_list[index+1] = "low"
                tides_list[index+2] = "medium-high"
                tides_list[index+3] = "medium-high"
                tides_list[index+4] = "medium-high"
                tides_list[index+5] = "medium-high"
                tides_list[index+6] = "high"
                tides_list[index+7] = "high"
            tide_counter = 0
            counter+=1
            continue
            
        if(tide == "low"):
            index = counter-tide_counter
            if (tide_counter == 3):
                tides_list[index] = "high"
                tides_list[index+1] = "medium-low"
                tides_list[index+2] = "low"
            if (tide_counter == 4):
                tides_list[index] = "high"
                tides_list[index+1] = "high"
                tides_list[index+2] = "medium-low"
                tides_list[index+3] = "low"
            if (tide_counter == 5):
                tides_list[index] = "high"
                tides_list[index+1] = "high"
                tides_list[index+2] = "medium-low"
                tides_list[index+3] = "low"
                tides_list[index+4] = "low"     
            if (tide_counter == 6):
                tides_list[index] = "high"
                tides_list[index+1] = "high"
                tides_list[index+2] = "medium-low"
                tides_list[index+3] = "medium-low"
                tides_list[index+4] = "low"
                tides_list[index+5] = "low"
            if (tide_counter == 7):
                tides_list[index] = "high"
                tides_list[index+1] = "high"
                tides_list[index+2] = "medium-low"
                tides_list[index+3] = "medium-low"
                tides_list[index+4] = "medium-low"
                tides_list[index+5] = "low"
                tides_list[index+6] = "low"
            if (tide_counter == 8):
                tides_list[index] = "high"
                tides_list[index+1] = "high"
                tides_list[index+2] = "medium-low"
                tides_list[index+3] = "medium-low"
                tides_list[index+4] = "medium-low"
                tides_list[index+5] = "medium-low"
                tides_list[index+6] = "low"
                tides_list[index+7] = "low"
            tide_counter = 0
            counter+=1
            continue
        
        counter+=1
        tide_counter+=1
    return tides_list
def set_real_tides(data,tides_list):
    counter = 0
    for tide in tides_list:
        if tide =="high":
            tides_list[counter] = 1
        if tide == "low":
            tides_list[counter] = 0
        if tide == "medium-high":
            tides_list[counter] = 0.5
        if tide == "medium-low":
            tides_list[counter] = 0.5
        if tide == "":
            tides_list[counter] = 0.5
        counter+=1
    for element in data:
        date = list(element.keys())[0]
        element[date]['tide'][0] = tides_list[data.index(element)]
        
def tides_to_string(tide):
    if(tide == 1):
        return "high"
    if(tide == 0):
        return "low"
    if(tide == 0.5):
        return "medium-low"

def set_calification(data):
    spots = config.spots
    counter = 0
    start = time.time()
    
    current_date = datetime.now()
    dt_string = current_date.strftime("%d/%m/%Y %H:%M:%S")
    current_time_hour = dt_string[11:13]
    current_time_day = dt_string[0:2]
    for x in data:
        date = list(x.keys())[0]
        current_hour = date[11:13]
        current_day = date[8:10]
        if (current_time_day == current_day and current_time_hour== current_hour): 
            new_data = {'swellDirection': x[date]['swellDirection'],
                    'swellHeight':x[date]['swellHeight'],
                    'swellPeriod':x[date]['swellPeriod'],
                    'windSpeed':x[date]['windSpeed'],
                    'windDirection':x[date]['windDirection'],
                    'tide':x[date]['tide']
                    }
            api_data = pd.DataFrame(data=new_data)
            print(date)
            for spot in spots:
                    print("Aplicando el modelo a "+ str(spot) + " vuelta " + str(counter))
                    calification = model(spot,api_data)
                    x[date][spot] = round(calification[0],1)


    end = time.time()
    print(end - start)
    
def model(spot,api_data):
    df = pd.read_csv (config.csv_calificated_history_path)
    x = df[['swellDirection','swellHeight','swellPeriod','windSpeed','windDirection','tide']]
    y = df[spot]
    regresion = LinearRegression()
    regresion.fit(x,y)
    
    prediccion = regresion.predict(api_data)
    # evaluacion = regresion.score(x_test, y_test)
    return prediccion
    
def transform_direction(direction):
    rounded_direction = round(direction)
    if rounded_direction in np.arange(0,10):
        return "N"
    if rounded_direction in np.arange(10,50):
        return "N-NE"
    if rounded_direction in np.arange(50,80):
        return "NE"
    if rounded_direction in np.arange(80,100):
        return "E"
    if rounded_direction in np.arange(100,140):
        return "S-SE"
    if rounded_direction in np.arange(140,170):
        return "SE"
    if rounded_direction in np.arange(170,190):
        return "S"
    if rounded_direction in np.arange(190,230):
        return "S-SO"
    if rounded_direction in np.arange(230,260):
        return "SO"
    if rounded_direction in np.arange(260,280):
        return "O"
    if rounded_direction in np.arange(280,320):
        return "O-NO"
    if rounded_direction in np.arange(320,350):
        return "NO"
    if rounded_direction in np.arange(350,360):
        return "N"

def web_json(aux_list):
    counter = 0
    current_date = datetime.now()
    dt_string = current_date.strftime("%d/%m/%Y %H:%M:%S")
    spots = config.spots
    
    calificated = False
    aux_data={}
    aux_data['headers'] = []
    aux_data['headers'].append('Params')
    aux_data['swellDirection'] = []
    aux_data['swellDirection'].append("Swell Direction")
    aux_data['swellHeight'] = []
    aux_data['swellHeight'].append("Swell Height (m)")
    aux_data['swellPeriod'] = []
    aux_data['swellPeriod'].append("Swell Period (s)")
    aux_data['windSpeed'] = []
    aux_data['windSpeed'].append("Wind Speed (m/s)")
    aux_data['windDirection'] = []
    aux_data['windDirection'].append("Wind Direction")
    aux_data['waterTemperature'] = []
    aux_data['waterTemperature'].append("Water Temperature (C)")
    aux_data['tide'] = []
    aux_data['tide'].append("Tide")
    aux_data['calification'] = []
    for date in aux_list:
        fecha = list(date.keys())[0]
        hora = fecha[11:13]
        dia = fecha[8:10]
        
        if(dt_string[0:2] == dia and hora == dt_string[11:13]):
            calification_dictionary = {}
            print("Current day: " +dt_string[0:2]+ " comparado con "+ dia + " y la hora "+ hora)
            for spot in spots:
                calification_dictionary[spot] = date[fecha][spot]
            aux_data['calification'].append(calification_dictionary)
            calificated = True
            
        if hora in config.web_hours:
            aux_data['headers'].append(dia +"  "+ hora + "h")
            aux_data['swellDirection'].append(transform_direction(date[fecha]['swellDirection'][0]))
            aux_data['swellHeight'].append(date[fecha]['swellHeight'][0])
            aux_data['swellPeriod'].append(date[fecha]['swellPeriod'][0])
            aux_data['windSpeed'].append(date[fecha]['windSpeed'][0])
            aux_data['windDirection'].append(transform_direction(date[fecha]['windDirection'][0]))
            aux_data['waterTemperature'].append(date[fecha]['waterTemperature'][0])
            aux_data['tide'].append(tides_to_string(date[fecha]['tide'][0]))        
            counter+=1

        if counter == 35 and calificated == True:
            break    
    with open(config.local_storage_json+'web.json', 'w') as fp:
        json.dump(aux_data, fp, indent  = 5)
    return aux_data


def cloud_function():
    # API FUNCTIONS
    # -------------------------
    # Recibo los datos de la API
    data = get_data_from_api()
    # Recibo las mareas de la API
    tides = get_tide_from_api()
    
    # Realizo una copia del JSON que recibo
    aux_data = copy.deepcopy(data)
    # Genero una lista de diccionarios con los datos
    aux_list = set_data(aux_data)
    
    # PREPARACIÓN MAREAS
    # -------------------------
    # Junto las mareas con los datos meteorológicos
    set_tides(aux_list,tides)
    # Calculo las mareas para todas las horas
    tides_list = calculate_tides(aux_list)
    # Transformo las mareas a equivalentes float para el modlo
    set_real_tides(aux_list,tides_list)
    
    # CALIFICACIÓN
    # -------------------------
    set_calification(aux_list)
    
    # JSON_FINAL_PREPARADO
    # -------------------------
    final_data = web_json(aux_list)
    return final_data
    # return aux_list





# res = cloud_function()



