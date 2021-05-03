import requests
import config
import json
import csv
import asyncio
import time
import copy
import xlsxwriter

#API para recuperar datos históricos con los que se creará un modelo de IA para calificar las rompientes
def api_1():
    response = requests.get(
      config.api_endpoint,
      params={
        'q': str(config.lat) +","+str(config.lng),
        'date': '2021-03-05',
        'endate': '2021-05-01',
        'format': 'json',
        'tide': 'yes',
        'key': str(config.api_key)
      }
    )
    json_data = response.json()
    return json_data

#2ª API para recuperar datos históricos con los que se creará un modelo de IA para calificar las rompientes
def api_2(start,end):

    response = requests.get(
      config.api2_endopoint,
      params={
        'lat': config.lat,
        'lng': config.lng,
        'params': config.params,
        'start': start,
        'end': end,
      },
      headers={
        'Authorization': config.api2_key
      }
    )
    json_data = response.json()
    return json_data

def api_3(start,end):
  response = requests.get(
  config.api_tide_endpoint,
  params={
    'lat': config.lat,
    'lng': config.lng,
    'start': start, 
    'end': end,  
  },
  headers={
    'Authorization': config.api2_key
  }
  )
  json_data = response.json()
  return json_data

def timer():
    start_time = time.time()
    seconds = 3
    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        if elapsed_time > seconds:
            break
        
# Método que llama a la API 2 y 3, para conseguir los datos desde 2017 hasta 2021
def allfreeRequests():
    json_swells_list = []
    json_tides_list = []
    data_dictionary = {}
    for year in range(2017,2021):
        for month in range(1,13):
            for day in range(1,30,10):
                start = str(year)+'-'+str(month).zfill(2)+'-'+str(day).zfill(2)+'T00:00:00+00:00'
                end = str(year)+'-'+str(month).zfill(2)+'-'+str(int(day)+9).zfill(2)+'T00:00:00+00:00'
                
                if (str(month).zfill(2) == '02' and end == str(year)+'-02-30T00:00:00+00:00'):
                    end = str(year)+'-'+str(month).zfill(2)+'-28'+'T00:00:00+00:00'
                print(start,end) 
                # lista 
                api2_result = api_2(start,end)
                api3_result = api_3(start,end)
                json_swells_list.append(api2_result)    
                json_tides_list.append(api3_result)
                # json_list.append((start,end))
    data_dictionary['swells'] = json_swells_list
    data_dictionary['tides'] = json_tides_list
    save_json(data_dictionary)
    dict_to_excel(dictionary_prepare(data_dictionary))
    return data_dictionary

# Método que guarda un archivo JSON
def save_json(json_data):
    with open("history.json", "w") as outfile: 
        json.dump(json_data, outfile, indent =7)

def open_json(json_data):
    with open('history.json') as json_file:
        data = json.load(json_file)
    return data

def json_to_csv(history_dictionary):
    a_file = open("history.csv", "w") 
    writer = csv.writer(history_dictionary)
    for key, value in history_dictionary.items():
        writer.writerow([key, value])  
    a_file.close()

def dictionary_prepare(dictionary):
    aux_dictionary = copy.deepcopy(dictionary)
    counter = 0
    for element in dictionary['tides']:
        
        for data in element['data']:
            date = data['time']
            day = date[0:10]
            time = date[11:16]
            hour = time[0:2]
            # minutes = time [3:5]
            tide_type = data['type']
            counter2 = 0
            for x in dictionary["swells"][counter]['hours']:
                day2=x["time"][0:10]
                hour2=x["time"][11:13]
                if(day == day2):
                    if(hour == hour2):
                        print(date,x["time"],tide_type)
                        print (counter, counter2)
                        aux_dictionary["swells"][counter]['hours'][counter2]['tide'] = tide_type     
                counter2 +=1
        counter +=1       
    return aux_dictionary
    
def dict_to_excel(dictionary):
    workbook = xlsxwriter.Workbook('history.xlsx')
    worksheet = workbook.add_worksheet()
    
    # Use the worksheet object to write
    # data via the write() method.
    worksheet.write('A1', 'time')
    worksheet.write('B1', 'swellDirection')
    worksheet.write('C1', 'swellHeight')
    worksheet.write('D1', 'swellPeriod')
    worksheet.write('E1', 'waterTemperature')
    worksheet.write('F1', 'windSpeed')
    worksheet.write('G1', 'windDirection')
    worksheet.write('H1', 'tide')
    
    counter = 1
    for element in dictionary['swells']:
        for hour in element['hours']:
            worksheet.write(counter, 0, hour['time'])
            if('swellDirection' in hour.keys()):
                worksheet.write(counter, 1, hour['swellDirection']['sg'])
            if('swellHeight' in hour.keys()):
                worksheet.write(counter, 2, hour['swellHeight']['sg'])
            if('swellPeriod' in hour.keys()):
                worksheet.write(counter, 3, hour['swellPeriod']['sg'])
            if('waterTemperature' in hour.keys()):
                worksheet.write(counter, 4, hour['waterTemperature']['sg'])
            if('windSpeed' in hour.keys()):
                worksheet.write(counter, 5, hour['windSpeed']['sg'])
            if('windDirection' in hour.keys()):
                worksheet.write(counter, 6, hour['windDirection']['sg'])  
            if('tide' in hour.keys()):
                worksheet.write(counter,7,hour['tide'])
            counter +=1
            # worksheet.write(counter,7,data['type'])
    workbook.close()
# a = api_2()
# dict_to_excel()
# save_json(allfreeRequests())
# a = allfreeRequests()
# b = api_2('2017-02-21T00:00:00+00:00', '2017-02-28T00:00:00+00:00')
