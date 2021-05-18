import config 
import pandas as pd
import numpy as np
import os

path = config.csv_history_path
new_path = os.path.dirname(path)
file_name = os.path.splitext(os.path.basename(path))

# Sardinero 1: /oeste/suroeste/sur - alta/media marea - +2m de mar de fondo
def set_calification_sardinero_uno(swellDirection, swellHeight, swellPeriod, windSpeed, windDirection, tide):
    calification = 0
    wind = False
    # Swell Direction 0.5
    if swellDirection in np.arange (180,360):
        if swellDirection in np.arange (290,330):
            calification +=1
        if swellDirection in np.arange (330,360):
            calification +=0.3
    if swellDirection in np.arange (0,180):
        if swellDirection in np.arange (0 ,30):
            calification +=0.3
        if swellDirection in np.arange (30,80):
            calification +=0.5
        if swellDirection in np.arange (90,180):
            calification +=0
            
    # Swell Height 2.5
    if swellHeight in np.arange (0,2):
        if swellHeight in np.arange (0,1):
            calification +=0
        if swellHeight in np.arange (1,1.5):
            calification +=0.7
        if swellHeight in np.arange (1.5,2):
            calification += 1
    if swellHeight in np.arange (2,12):
        if swellHeight in np.arange (2,4):
            calification +=2.5
        if swellHeight in np.arange (4,5):
            calification +=2
        if swellHeight in np.arange (5,12):
            calification +=1
    
    # Swell Period 3
    if swellPeriod in np.arange (0,10):
        calification +=round(swellPeriod/10,2)
    elif swellPeriod in np.arange (10,15):
        if swellPeriod in np.arange (10,12):
            calification +=1
        if swellPeriod in np.arange (12,15):
            calification +=2
    elif swellPeriod >=15:
            calification +=3
            
    # Wind Direction 2
    if windDirection in range (180,360):
        if windDirection in range (180,290):
            wind = True
            calification +=2
        if windDirection in range (290,360):
            calification +=0.5
    if windDirection in range (0,180):
        if windDirection in range (0 ,120):
            calification +=0
        elif windDirection in range (120,160):
            calification +=0.5
        elif windDirection in range (160,180):
            calification +=1
    
    # Wind Speed 1
    if wind == True:
        if windSpeed in np.arange (0,7):
            if windSpeed in np.arange (0,3):
                calification +=0.3
            if windSpeed in np.arange (3,7):
                calification +=1
        elif windSpeed > 7:
            if windSpeed in np.arange (7,11):
                calification +=0.8
            elif windSpeed in np.arange (11,14):
                calification +=0.5
            elif windSpeed in np.arange (14,15):
                calification +=0.2
            elif windSpeed >= 15:
                calification +=0
                
    if wind == False:
        if windSpeed in np.arange (0,7):
            if windSpeed in np.arange (0,3):
                calification +=0.5
            if windSpeed in np.arange (3,7):
                calification +=0.4
        elif windSpeed >= 7:
            if windSpeed in np.arange (7,11):
                calification +=0.3
            elif windSpeed in np.arange (11,14):
                calification +=0.1
            elif windSpeed >= 14:
                calification +=0
            
    # Tide 1
    if tide == "low":
        calification +=0.5
    if tide == "medium-low" :
        calification +=0.7
    if tide == "medium-high":
        calification += 1
    if tide == "high":
        calification+=0.5
          
#  Lo mismo q el 1 pero añadiendo noroeste a los vientos y quitando sur
def set_calification_sardinero_dos(swellDirection, swellHeight, swellPeriod, windSpeed, windDirection, tide):
    calification = 0
    wind = False
    # Swell Direction 0.5
    if swellDirection in range (180,360):
        if swellDirection in range (290,330):
            calification +=1
        if swellDirection in range (330,360):
            calification +=0.3
    if swellDirection in range (0,180):
        if swellDirection in range (0 ,30):
            calification +=0.3
        if swellDirection in range (30,80):
            calification +=0.5
        if swellDirection in range (90,180):
            calification +=0
            
    # Swell Height 2.5
    if swellHeight in range (0,2):
        if swellHeight in range (0,1):
            calification +=0
        if swellHeight in range (1,1.5):
            calification +=0.7
        if swellHeight in range (1.5,2):
            calification += 1
    if swellHeight in range (2,12):
        if swellHeight in range (2,4):
            calification +=2.5
        if swellHeight in range (4,5):
            calification +=2
        if swellHeight in range (5,12):
            calification +=1
    
    # Swell Period 3
    if swellPeriod in range (0,10):
        calification +=round(swellPeriod/10,2)
    elif swellPeriod in range (10,15):
        if swellPeriod in range (10,12):
            calification +=1
        if swellPeriod in range (12,15):
            calification +=2
    elif swellPeriod >=15:
            calification +=3
            
    # Wind Direction 2
    if windDirection in range (180,360):
        if windDirection in range (180,290):
            wind = True
            calification +=2
        if windDirection in range (290,360):
            calification +=0.5
    if windDirection in range (0,180):
        if windDirection in range (0 ,120):
            calification +=0
        elif windDirection in range (120,160):
            calification +=0.5
        elif windDirection in range (160,180):
            calification +=1
    
    # Wind Speed 1
    if wind== True:
        if windSpeed in range (0,7):
            if windSpeed in range (0,3):
                calification +=0.3
            if windSpeed in range (3,7):
                calification +=1
        elif windSpeed > 7:
            if windSpeed in range (7,11):
                calification +=0.8
            elif windSpeed in range (11,14):
                calification +=0.5
            elif windSpeed in range (14,15):
                calification +=0.2
            elif windSpeed >= 15:
                calification +=0
                
    if wind == False:
        if windSpeed in range (0,7):
            if windSpeed in range (0,3):
                calification +=0.5
            if windSpeed in range (3,7):
                calification +=0.4
        elif windSpeed >= 7:
            if windSpeed in range (7,11):
                calification +=0.3
            elif windSpeed in range (11,14):
                calification +=0.1
            elif windSpeed >= 14:
                calification +=0
            
    # Tide 1
    if tide == "low":
        calification +=0.5
    if tide == "medium-low ":
        calification +=0.7
    if tide == "medium-high":
        calification += 1
    if tide == "high":
        calification+=0.5       
# noroeste/oeste/suroeste/sur - marea baja -  +2m de mar de fondo
def set_calification_mataleñas(swellDirection, swellHeight, swellPeriod, windSpeed, windDirection, tide):
    calification = 0

# este/sureste/sur/suroeste - todas las mareas aunque lo mejor es media (dependiendo del coef) - 1'1a 2m de mar de fondo
def set_calification_cañones(swellDirection, swellHeight, swellPeriod, windSpeed, windDirection, tide):
    calification = 0
# nordeste/este/sureste/sur/suroeste - 2 horas subiendo hasta 2 horas antes de la plea - 1'3m a 2m de mar de fondo
def set_calification_rosamunda(swellDirection, swellHeight, swellPeriod, windSpeed, windDirection, tide):
    calification = 0
# este/sureste/sur/suroeste - todas las mareas (depende de los fondos) - 0'5 a 1'8m de mar de fondo (depende del mar que aguanten los fondos) 
def set_calification_valdearenas(swellDirection, swellHeight, swellPeriod, windSpeed, windDirection, tide):
    calification = 0
# este/sureste/sur/suroeste - todas las mareas (depende de los fondos) - 0'5 a 1'8m de mar de fondo (depende del mar que aguanten los fondos) 
def set_calification_canallave(swellDirection, swellHeight, swellPeriod, windSpeed, windDirection, tide):
    calification = 0
    
#  suroeste/sur/sureste/este (en loredo nordeste) - todas las mareas (depende de los fondos) - 0'8 a 1'8m de mar de fondo
def set_calification_somo(swellDirection, swellHeight, swellPeriod, windSpeed, windDirection, tide):
    calification = 0
    
# oeste flojo/suroeste/sur/sureste - todas las mareas ( depende de los fondos) - 1'5 a 2'5m de mar de fondo 
def set_calification_langre(swellDirection, swellHeight, swellPeriod, windSpeed, windDirection, tide):
    calification = 0
    
# oeste (flojo)/suroeste/sur/sureste - marea baja- 1'3 a 2m de mar de fondo 
def set_calification_usgo(swellDirection, swellHeight, swellPeriod, windSpeed, windDirection, tide):
    calification = 0
    
# nordeste/este/sureste/sur/suroeste - normalmente marea baja, pero puede romper en todas las mareas depende de los fondos - 0'8 a 2m de mar de fondo ( si esta epic el fondo aguanta mar) 
def set_calification_gerra(swellDirection, swellHeight, swellPeriod, windSpeed, windDirection, tide):
    calification = 0
    
# oeste (flojo)/suroeste/sur/sureste - marea media/baja - 1'8 a 3m de mar de fondo
def set_calification_farolillo(swellDirection, swellHeight, swellPeriod, windSpeed, windDirection, tide):
    calification = 0
    
# sureste/sur/suroeste - media marea/alta - 1'7 a 4m de mar de fondo
def set_calification_brusco(swellDirection, swellHeight, swellPeriod, windSpeed, windDirection, tide):
    calification = 0
    
# nordeste/este/sureste/sur (flojo) - hora y media subiendo la marea hasta la plea -   +1'9 m de mar de fondo
def set_calification_santamarina(swellDirection, swellHeight, swellPeriod, windSpeed, windDirection, tide):
    calification = 0
    
def set_calification_fortaleza(swellDirection, swellHeight, swellPeriod, windSpeed, windDirection, tide):
    calification = 0
    
def set_calification_laredo(swellDirection, swellHeight, swellPeriod, windSpeed, windDirection, tide):
    calification = 0

df = df = pd.read_csv(new_path+"/"+file_name[0]+".csv")
def set_all_califications(csv_file):
    for i in range(len(csv_file)):
        csv_file['sardinero_uno'][i] = set_calification_sardinero_uno(csv_file.loc[i,'swellDirection'],csv_file.loc[i,'swellHeight'],csv_file.loc[i,'swellPeriod'],csv_file.loc[i,'windSpeed'],csv_file.loc[i,'windDirection'],csv_file.loc[i,'tide'])
        # set_calification_sardinero_uno(row['swellDirection'],row['swellHeight'],row['swellPeriod'],row['windSpeed'],row['windDirection'],row['tide'])


a = set_all_califications(df)