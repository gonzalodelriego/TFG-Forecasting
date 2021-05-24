# importing the requests library
import requests
import config
import pandas as pd
import time
import json
import copy
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
       aux_data_dict['swellDirection'] = [x['swellDirection']['sg']]
       aux_data_dict['swellHeight'] = [x['swellHeight']['sg']]
       aux_data_dict['swellPeriod'] = [x['swellPeriod']['sg']]
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
    
def set_calification(data):
    spots = config.spots
    counter = 0
    start = time.time()
    for x in data:
        date = list(x.keys())[0]
        new_data = {'swellDirection': x[date]['swellDirection'],
            'swellHeight':x[date]['swellHeight'],
            'swellPeriod':x[date]['swellPeriod'],
            'windSpeed':x[date]['windSpeed'],
            'windDirection':x[date]['windDirection'],
            'tide':x[date]['tide']
            }
        api_data = pd.DataFrame(data=new_data)
        counter+=1
        for spot in spots:
            print("Aplicando el modelo a "+ str(spot) + " vuelta " + str(counter))
            calification = model(spot,api_data)
            x[date][spot] = calification
        if counter == 236:
            break
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
    
def tides_to_string(tide):
    if(tide == 1):
        return "high"
    if(tide == 0):
        return "low"
    if(tide == 0.5):
        return "medium-low"
def cloud_function():
    data = get_data_from_api()
    aux_data = copy.deepcopy(data)
    aux_list = set_data(aux_data)
    tides = get_tide_from_api()
    set_tides(aux_list,tides)
    # FALTAN DE CALCULAR TODAS LAS MAREAS las ultimas 4
    tides_list = calculate_tides(aux_list)
    set_real_tides(aux_list,tides_list)
    set_calification(aux_list)
    final_data = web_json(aux_list)
    return final_data

# def web_json(aux_list):
#     web_dictionary = {}
#     spots = config.spots
#     hours = config.web_hours
#     for date in aux_list:
#         fecha = list(date.keys())[0]
#         day = fecha[8:10]
#         if day not in web_dictionary:
#             web_dictionary[day] = {}
#         for hour in hours:
#             hora = fecha[11:13]
#             if hour not in web_dictionary[day]:
#                 web_dictionary[day][hour] = {}
#             if hour in web_dictionary[day]:
#                 if(hour == hora):
#                     web_dictionary[day][hour]['swellDirection'] = date[fecha]['swellDirection'][0]
#                     web_dictionary[day][hour]['swellHeight'] = date[fecha]['swellHeight'][0]
#                     web_dictionary[day][hour]['swellPeriod'] = date[fecha]['swellPeriod'][0]
#                     web_dictionary[day][hour]['windSpeed'] = date[fecha]['windSpeed'][0]
#                     web_dictionary[day][hour]['windDirection'] = date[fecha]['windDirection'][0]
#                     web_dictionary[day][hour]['tide'] = tides_to_string(date[fecha]['tide'][0])
#                     calification_dictionary = {}
#                     for spot in spots:
#                         calification_dictionary[spot] = date[fecha][spot][0]
#                     web_dictionary[day][hour]['califications'] = calification_dictionary
        
#         if (len(web_dictionary)== 8):
#             break
#     web_dictionary.popitem()
    # with open(config.local_storage_json+'web.json', 'w') as fp:
    #     json.dump(web_dictionary, fp)
#     return web_dictionary

# def web_json(aux_list,data):
#     spots = config.spots
#     aux_data = {}
#     aux_data['hours'] = []
#     for date in data['hours']:
#         time = date['time']
#         # print(time)
#         hora = time[11:13]
#         for x in aux_list:
#             fecha = list(x.keys())[0]
#             # print(time,fecha)
#             if(time == fecha):
#                 # print("entreo aqui")
#                 calification_dictionary = {}
#                 for spot in spots:
#                     if x[fecha][spot] != 0:
#                         calification_dictionary[spot] = x[fecha][spot][0]
#                     if x[fecha][spot] == 0:
#                         calification_dictionary = x[fecha][spot]
#                 date['calification'] =  calification_dictionary
#                 date['tide'] = tides_to_string(x[fecha]['tide'][0])
#         if hora in config.web_hours:
#             aux_data['hours'].append(date)
    
#     return aux_data

# def web_json(aux_list):
#     counter = 0
#     spots = config.spots
#     aux_data={}
#     aux_data['headers'] = []
#     aux_data['headers'].append('Params')
#     aux_data['rows'] = []
#     swellDirection = []
#     swellDirection.append("Swell Direction")
#     swellHeight = []
#     swellHeight.append("Swell Height")
#     swellPeriod = []
#     swellPeriod.append("Swell Period")
#     windSpeed = []
#     windSpeed.append("Wind Speed")
#     windDirection = []
#     windDirection.append("Wind Direction")
#     # waterTemperature = []
#     tide = []
#     tide.append("Tide")
#     calification = []
#     for date in aux_list:
#         fecha = list(date.keys())[0]
#         hora = fecha[11:13]
#         dia = fecha[8:10]
#         if hora in config.web_hours:
#             aux_data['headers'].append(dia +" "+ hora + "h")
#             swellDirection.append(date[fecha]['swellDirection'][0])
#             swellHeight.append(date[fecha]['swellHeight'][0])
#             swellPeriod.append(date[fecha]['swellPeriod'][0])
#             windSpeed.append(date[fecha]['windSpeed'][0])
#             windDirection.append(date[fecha]['windDirection'][0])
#             # waterTemperature.append(date[hora]['waterTemperature'][0])
#             tide.append(tides_to_string(date[fecha]['tide'][0]))
#             calification_dictionary = {}
#             for spot in spots:
#                 if date[fecha][spot] != 0:
#                     calification_dictionary[spot] = date[fecha][spot][0]
#                 if date[fecha][spot] == 0:
#                     calification_dictionary = date[fecha][spot]
#             calification.append(calification_dictionary)
#             counter+=1
#         if counter == 35:
#             break
#     aux_data['rows'].append(swellDirection)
#     aux_data['rows'].append(swellHeight)
#     aux_data['rows'].append(swellPeriod)
#     aux_data['rows'].append(windSpeed)
#     aux_data['rows'].append(windDirection)
#     aux_data['rows'].append(tide)
#     aux_data['rows'].append(calification)
    
    
#     return aux_data

def web_json(aux_list):
    counter = 0
    spots = config.spots
    aux_data={}
    aux_data['headers'] = []
    aux_data['headers'].append('Params')
    aux_data['swellDirection'] = []
    aux_data['swellDirection'].append("Swell Direction")
    aux_data['swellHeight'] = []
    aux_data['swellHeight'].append("Swell Height")
    aux_data['swellPeriod'] = []
    aux_data['swellPeriod'].append("Swell Period")
    aux_data['windSpeed'] = []
    aux_data['windSpeed'].append("Wind Speed")
    aux_data['windDirection'] = []
    aux_data['windDirection'].append("Wind Direction")
    # waterTemperature = []
    aux_data['tide'] = []
    aux_data['tide'].append("Tide")
    aux_data['calification'] = []
    for date in aux_list:
        fecha = list(date.keys())[0]
        hora = fecha[11:13]
        dia = fecha[8:10]
        if hora in config.web_hours:
            aux_data['headers'].append(dia +" "+ hora + "h")
            aux_data['swellDirection'].append(date[fecha]['swellDirection'][0])
            aux_data['swellHeight'].append(date[fecha]['swellHeight'][0])
            aux_data['swellPeriod'].append(date[fecha]['swellPeriod'][0])
            aux_data['windSpeed'].append(date[fecha]['windSpeed'][0])
            aux_data['windDirection'].append(date[fecha]['windDirection'][0])
            # waterTemperature.append(date[hora]['waterTemperature'][0])
            aux_data['tide'].append(tides_to_string(date[fecha]['tide'][0]))
            calification_dictionary = {}
            for spot in spots:
                if date[fecha][spot] != 0:
                    calification_dictionary[spot] = date[fecha][spot][0]
                if date[fecha][spot] == 0:
                    calification_dictionary = date[fecha][spot]
            aux_data['calification'].append(calification_dictionary)
            counter+=1
        if counter == 35:
            break    
    with open(config.local_storage_json+'web.json', 'w') as fp:
        json.dump(aux_data, fp, indent  = 5)
    return aux_data
res = cloud_function()



