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
    swellCalification = 0
    swellHeightCalification = 0
    swellPeriodCalification = 0
    windSpeedCalification = 0
    windDirectionCalification = 0
    tideCalification = 0
    wind = False
    
    
    if not np.isnan(swellDirection or swellHeight or swellPeriod or windSpeed or windDirection):
        swellDir = round(swellDirection)
        swellH = round(swellHeight)
        swellP = round(swellPeriod)
        windS =  round(windSpeed)
        windD = round(windDirection)
    if np.isnan(swellDirection or swellHeight or swellPeriod or windSpeed or windDirection):
        swellDir = swellDirection
        swellH = swellHeight
        swellP = swellPeriod
        windS =  windSpeed
        windD = windDirection
    # if not np.isnan(swellDirection or swellHeight or swellPeriod or windSpeed or windDirection):
    # Swell Direction 0.5
    if swellDir in np.arange (180,360):
        if swellDir in np.arange (270,330):
            swellCalification +=1
        if swellDir in np.arange (330,360):
            swellCalification +=0.3
    if swellDir in np.arange (0,180):
        if swellDir in np.arange (0 ,30):
            swellCalification +=0.3
        if swellDir in np.arange (30,80):
            swellCalification +=0.5
        if swellDir in np.arange (90,180):
            swellCalification +=0
    
    # Swell Height 2.5
    if swellH in np.arange (0,2):
        if swellH in np.arange (0,1):
            swellHeightCalification +=0
        if swellH in np.arange (1,1.5):
            swellHeightCalification +=0.7
        if swellH in np.arange (1.5,2):
            swellHeightCalification += 1
    if swellH in np.arange (2,12):
        if swellH in np.arange (2,4):
            swellHeightCalification +=2.5
        if swellH in np.arange (4,5):
            swellHeightCalification +=2
        if swellH >=5:
            swellHeightCalification +=1
    # Swell Period 3
    if swellP in np.arange (0,10):
        swellPeriodCalification +=round(swellPeriod/10,2)
    elif swellP in np.arange (10,15):
        if swellP in np.arange (10,12):
            swellPeriodCalification +=1
        if swellP in np.arange (12,15):
            swellPeriodCalification +=2
    elif swellP >=15:
            swellPeriodCalification +=3
            
    # Wind Direction 2
    if windD in np.arange (180,360):
        if windD in np.arange (180,290):
            wind = True
            windDirectionCalification +=2
        if windD in np.arange (290,360):
            windDirectionCalification +=0.5
    if windD in np.arange (0,180):
        if windD in np.arange (0 ,120):
            windDirectionCalification +=0
        elif windD in np.arange (120,160):
            windDirectionCalification +=0.5
        elif windD in np.arange (160,180):
            windDirectionCalification +=1
    
    # Wind Speed 1
    if wind == True:
        if windS in np.arange (0,7):
            if windS in np.arange (0,3):
                windSpeedCalification +=0.3
            if windS in np.arange (3,7):
                windSpeedCalification +=1
        elif windS > 7:
            if windS in np.arange (7,11):
                windSpeedCalification +=0.8
            elif windS in np.arange (11,14):
                windSpeedCalification +=0.5
            elif windS in np.arange (14,15):
                windSpeedCalification +=0.2
            elif windS >= 15:
                windSpeedCalification +=0
                
    if wind == False:
        if windS in np.arange (0,7):
            if windS in np.arange (0,3):
                windSpeedCalification +=0.5
            if windS in np.arange (3,7):
                windSpeedCalification +=0.4
        elif windS >= 7:
            if windS in np.arange (7,11):
                windSpeedCalification +=0.3
            elif windS in np.arange (11,14):
                windSpeedCalification +=0.1
            elif windS >= 14:
                windSpeedCalification +=0
            
    # Tide 1
    if tide == "low":
        tideCalification +=0.5
    if tide == "medium-low" :
        tideCalification +=0.7
    if tide == "medium-high":
        tideCalification += 1
    if tide == "high":
        tideCalification+=0.5
    calification = tideCalification+windSpeedCalification+windDirectionCalification+swellHeightCalification+swellPeriodCalification+swellCalification
    
    # print("La puntuación del swell " + str(swellDirection)+" es: " +str(swellCalification))
    # print("La puntuación del tamaño de swell " + str(swellHeight)+" es: " +str(swellHeightCalification))
    # print("La puntuación del periodo del swell " + str(swellPeriod)+" es: " +str(swellPeriodCalification))
    # print("La puntuación de la direccion del viento " + str(windDirection)+" es: " +str(windDirectionCalification))
    # print("La puntuación de la velocidad del viento " + str(windSpeed)+" es: " +str(windSpeedCalification))
    # print("La puntuación de la marea " + str(tide)+" es: " +str(tideCalification))
    
    return calification
#  Lo mismo q el 1 pero añadiendo noroeste a los vientos y quitando sur
def set_calification_sardinero_dos(swellDirection, swellHeight, swellPeriod, windSpeed, windDirection, tide):
    calification = 0
    swellCalification = 0
    swellHeightCalification = 0
    swellPeriodCalification = 0
    windSpeedCalification = 0
    windDirectionCalification = 0
    tideCalification = 0
    wind = False
    
    
    if not np.isnan(swellDirection or swellHeight or swellPeriod or windSpeed or windDirection):
        swellDir = round(swellDirection)
        swellH = round(swellHeight)
        swellP = round(swellPeriod)
        windS =  round(windSpeed)
        windD = round(windDirection)
    if np.isnan(swellDirection or swellHeight or swellPeriod or windSpeed or windDirection):
        swellDir = swellDirection
        swellH = swellHeight
        swellP = swellPeriod
        windS =  windSpeed
        windD = windDirection
    # if not np.isnan(swellDirection or swellHeight or swellPeriod or windSpeed or windDirection):
    # Swell Direction 0.5
    if swellDir in np.arange (180,360):
        if swellDir in np.arange (270,330):
            swellCalification +=1
        if swellDir in np.arange (330,360):
            swellCalification +=0.3
    if swellDir in np.arange (0,180):
        if swellDir in np.arange (0 ,30):
            swellCalification +=0.3
        if swellDir in np.arange (30,80):
            swellCalification +=0.5
        if swellDir in np.arange (90,180):
            swellCalification +=0
    
    # Swell Height 2.5
    if swellH in np.arange (0,2):
        if swellH in np.arange (0,1):
            swellHeightCalification +=0
        if swellH in np.arange (1,1.5):
            swellHeightCalification +=0.7
        if swellH in np.arange (1.5,2):
            swellHeightCalification += 1
    if swellH in np.arange (2,12):
        if swellH in np.arange (2,4):
            swellHeightCalification +=2.5
        if swellH in np.arange (4,5):
            swellHeightCalification +=2
        if swellH >=5:
            swellHeightCalification +=1
    # Swell Period 3
    if swellP in np.arange (0,10):
        swellPeriodCalification +=round(swellPeriod/10,2)
    elif swellP in np.arange (10,15):
        if swellP in np.arange (10,12):
            swellPeriodCalification +=1
        if swellP in np.arange (12,15):
            swellPeriodCalification +=2
    elif swellP >=15:
            swellPeriodCalification +=3
            
    # Wind Direction 2
    if windD in np.arange (180,360):
        if windD in np.arange (180,290):
            wind = True
            windDirectionCalification +=2
        if windD in np.arange (290,360):
            windDirectionCalification +=0.5
    if windD in np.arange (0,180):
        if windD in np.arange (0 ,120):
            windDirectionCalification +=0
        elif windD in np.arange (120,160):
            windDirectionCalification +=0.5
        elif windD in np.arange (160,180):
            windDirectionCalification +=1
    
    # Wind Speed 1
    if wind == True:
        if windS in np.arange (0,7):
            if windS in np.arange (0,3):
                windSpeedCalification +=0.3
            if windS in np.arange (3,7):
                windSpeedCalification +=1
        elif windS > 7:
            if windS in np.arange (7,11):
                windSpeedCalification +=0.8
            elif windS in np.arange (11,14):
                windSpeedCalification +=0.5
            elif windS in np.arange (14,15):
                windSpeedCalification +=0.2
            elif windS >= 15:
                windSpeedCalification +=0
                
    if wind == False:
        if windS in np.arange (0,7):
            if windS in np.arange (0,3):
                windSpeedCalification +=0.5
            if windS in np.arange (3,7):
                windSpeedCalification +=0.4
        elif windS >= 7:
            if windS in np.arange (7,11):
                windSpeedCalification +=0.3
            elif windS in np.arange (11,14):
                windSpeedCalification +=0.1
            elif windS >= 14:
                windSpeedCalification +=0
            
    # Tide 1
    if tide == "low":
        tideCalification +=0.5
    if tide == "medium-low" :
        tideCalification +=0.7
    if tide == "medium-high":
        tideCalification += 1
    if tide == "high":
        tideCalification+=0.5
    calification = tideCalification+windSpeedCalification+windDirectionCalification+swellHeightCalification+swellPeriodCalification+swellCalification
    
    # print("La puntuación del swell " + str(swellDirection)+" es: " +str(swellCalification))
    # print("La puntuación del tamaño de swell " + str(swellHeight)+" es: " +str(swellHeightCalification))
    # print("La puntuación del periodo del swell " + str(swellPeriod)+" es: " +str(swellPeriodCalification))
    # print("La puntuación de la direccion del viento " + str(windDirection)+" es: " +str(windDirectionCalification))
    # print("La puntuación de la velocidad del viento " + str(windSpeed)+" es: " +str(windSpeedCalification))
    # print("La puntuación de la marea " + str(tide)+" es: " +str(tideCalification))
    
    return calification       
# noroeste/oeste/suroeste/sur - marea baja -  +2m de mar de fondo
def set_calification_mataleñas(swellDirection, swellHeight, swellPeriod, windSpeed, windDirection, tide):
    calification = 0
    swellCalification = 0
    swellHeightCalification = 0
    swellPeriodCalification = 0
    windSpeedCalification = 0
    windDirectionCalification = 0
    tideCalification = 0
    wind = False
    
    
    if not np.isnan(swellDirection or swellHeight or swellPeriod or windSpeed or windDirection):
        swellDir = round(swellDirection)
        swellH = round(swellHeight)
        swellP = round(swellPeriod)
        windS =  round(windSpeed)
        windD = round(windDirection)
    if np.isnan(swellDirection or swellHeight or swellPeriod or windSpeed or windDirection):
        swellDir = swellDirection
        swellH = swellHeight
        swellP = swellPeriod
        windS =  windSpeed
        windD = windDirection
    # if not np.isnan(swellDirection or swellHeight or swellPeriod or windSpeed or windDirection):
    # Swell Direction 0.5
    if swellDir in np.arange (180,360):
        if swellDir in np.arange (270,330):
            swellCalification +=1
        if swellDir in np.arange (330,360):
            swellCalification +=0.3
    if swellDir in np.arange (0,180):
        if swellDir in np.arange (0 ,30):
            swellCalification +=0.3
        if swellDir in np.arange (30,80):
            swellCalification +=0.5
        if swellDir in np.arange (90,180):
            swellCalification +=0
    
    # Swell Height 2.5
    if swellH in np.arange (0,2):
        if swellH in np.arange (0,1):
            swellHeightCalification +=0
        if swellH in np.arange (1,1.5):
            swellHeightCalification +=0.7
        if swellH in np.arange (1.5,2):
            swellHeightCalification += 1
    if swellH in np.arange (2,12):
        if swellH in np.arange (2,4):
            swellHeightCalification +=2.5
        if swellH in np.arange (4,5):
            swellHeightCalification +=2
        if swellH >=5:
            swellHeightCalification +=1
    # Swell Period 3
    if swellP in np.arange (0,10):
        swellPeriodCalification +=round(swellPeriod/10,2)
    elif swellP in np.arange (10,15):
        if swellP in np.arange (10,12):
            swellPeriodCalification +=1
        if swellP in np.arange (12,15):
            swellPeriodCalification +=2
    elif swellP >=15:
            swellPeriodCalification +=3
            
    # Wind Direction 2
    if windD in np.arange (180,360):
        if windD in np.arange (180,290):
            wind = True
            windDirectionCalification +=2
        if windD in np.arange (290,360):
            windDirectionCalification +=0.5
    if windD in np.arange (0,180):
        if windD in np.arange (0 ,120):
            windDirectionCalification +=0
        elif windD in np.arange (120,160):
            windDirectionCalification +=0.5
        elif windD in np.arange (160,180):
            windDirectionCalification +=1
    
    # Wind Speed 1
    if wind == True:
        if windS in np.arange (0,7):
            if windS in np.arange (0,3):
                windSpeedCalification +=0.3
            if windS in np.arange (3,7):
                windSpeedCalification +=1
        elif windS > 7:
            if windS in np.arange (7,11):
                windSpeedCalification +=0.8
            elif windS in np.arange (11,14):
                windSpeedCalification +=0.5
            elif windS in np.arange (14,15):
                windSpeedCalification +=0.2
            elif windS >= 15:
                windSpeedCalification +=0
                
    if wind == False:
        if windS in np.arange (0,7):
            if windS in np.arange (0,3):
                windSpeedCalification +=0.5
            if windS in np.arange (3,7):
                windSpeedCalification +=0.4
        elif windS >= 7:
            if windS in np.arange (7,11):
                windSpeedCalification +=0.3
            elif windS in np.arange (11,14):
                windSpeedCalification +=0.1
            elif windS >= 14:
                windSpeedCalification +=0
            
    # Tide 1
    if tide == "low":
        tideCalification +=0.5
    if tide == "medium-low" :
        tideCalification +=0.7
    if tide == "medium-high":
        tideCalification += 1
    if tide == "high":
        tideCalification+=0.5
    calification = tideCalification+windSpeedCalification+windDirectionCalification+swellHeightCalification+swellPeriodCalification+swellCalification
    
    # print("La puntuación del swell " + str(swellDirection)+" es: " +str(swellCalification))
    # print("La puntuación del tamaño de swell " + str(swellHeight)+" es: " +str(swellHeightCalification))
    # print("La puntuación del periodo del swell " + str(swellPeriod)+" es: " +str(swellPeriodCalification))
    # print("La puntuación de la direccion del viento " + str(windDirection)+" es: " +str(windDirectionCalification))
    # print("La puntuación de la velocidad del viento " + str(windSpeed)+" es: " +str(windSpeedCalification))
    # print("La puntuación de la marea " + str(tide)+" es: " +str(tideCalification))
    
    return calification

# este/sureste/sur/suroeste - todas las mareas aunque lo mejor es media (dependiendo del coef) - 1'1a 2m de mar de fondo
def set_calification_cañones(swellDirection, swellHeight, swellPeriod, windSpeed, windDirection, tide):
    calification = 0
    swellCalification = 0
    swellHeightCalification = 0
    swellPeriodCalification = 0
    windSpeedCalification = 0
    windDirectionCalification = 0
    tideCalification = 0
    wind = False
    
    
    if not np.isnan(swellDirection or swellHeight or swellPeriod or windSpeed or windDirection):
        swellDir = round(swellDirection)
        swellH = round(swellHeight)
        swellP = round(swellPeriod)
        windS =  round(windSpeed)
        windD = round(windDirection)
    if np.isnan(swellDirection or swellHeight or swellPeriod or windSpeed or windDirection):
        swellDir = swellDirection
        swellH = swellHeight
        swellP = swellPeriod
        windS =  windSpeed
        windD = windDirection
    # if not np.isnan(swellDirection or swellHeight or swellPeriod or windSpeed or windDirection):
    # Swell Direction 0.5
    if swellDir in np.arange (180,360):
        if swellDir in np.arange (270,330):
            swellCalification +=1
        if swellDir in np.arange (330,360):
            swellCalification +=0.3
    if swellDir in np.arange (0,180):
        if swellDir in np.arange (0 ,30):
            swellCalification +=0.3
        if swellDir in np.arange (30,80):
            swellCalification +=0.5
        if swellDir in np.arange (90,180):
            swellCalification +=0
    
    # Swell Height 2.5
    if swellH in np.arange (0,2):
        if swellH in np.arange (0,1):
            swellHeightCalification +=0
        if swellH in np.arange (1,1.5):
            swellHeightCalification +=0.7
        if swellH in np.arange (1.5,2):
            swellHeightCalification += 1
    if swellH in np.arange (2,12):
        if swellH in np.arange (2,4):
            swellHeightCalification +=2.5
        if swellH in np.arange (4,5):
            swellHeightCalification +=2
        if swellH >=5:
            swellHeightCalification +=1
    # Swell Period 3
    if swellP in np.arange (0,10):
        swellPeriodCalification +=round(swellPeriod/10,2)
    elif swellP in np.arange (10,15):
        if swellP in np.arange (10,12):
            swellPeriodCalification +=1
        if swellP in np.arange (12,15):
            swellPeriodCalification +=2
    elif swellP >=15:
            swellPeriodCalification +=3
            
    # Wind Direction 2
    if windD in np.arange (180,360):
        if windD in np.arange (180,290):
            wind = True
            windDirectionCalification +=2
        if windD in np.arange (290,360):
            windDirectionCalification +=0.5
    if windD in np.arange (0,180):
        if windD in np.arange (0 ,120):
            windDirectionCalification +=0
        elif windD in np.arange (120,160):
            windDirectionCalification +=0.5
        elif windD in np.arange (160,180):
            windDirectionCalification +=1
    
    # Wind Speed 1
    if wind == True:
        if windS in np.arange (0,7):
            if windS in np.arange (0,3):
                windSpeedCalification +=0.3
            if windS in np.arange (3,7):
                windSpeedCalification +=1
        elif windS > 7:
            if windS in np.arange (7,11):
                windSpeedCalification +=0.8
            elif windS in np.arange (11,14):
                windSpeedCalification +=0.5
            elif windS in np.arange (14,15):
                windSpeedCalification +=0.2
            elif windS >= 15:
                windSpeedCalification +=0
                
    if wind == False:
        if windS in np.arange (0,7):
            if windS in np.arange (0,3):
                windSpeedCalification +=0.5
            if windS in np.arange (3,7):
                windSpeedCalification +=0.4
        elif windS >= 7:
            if windS in np.arange (7,11):
                windSpeedCalification +=0.3
            elif windS in np.arange (11,14):
                windSpeedCalification +=0.1
            elif windS >= 14:
                windSpeedCalification +=0
            
    # Tide 1
    if tide == "low":
        tideCalification +=0.5
    if tide == "medium-low" :
        tideCalification +=0.7
    if tide == "medium-high":
        tideCalification += 1
    if tide == "high":
        tideCalification+=0.5
    calification = tideCalification+windSpeedCalification+windDirectionCalification+swellHeightCalification+swellPeriodCalification+swellCalification
    
    # print("La puntuación del swell " + str(swellDirection)+" es: " +str(swellCalification))
    # print("La puntuación del tamaño de swell " + str(swellHeight)+" es: " +str(swellHeightCalification))
    # print("La puntuación del periodo del swell " + str(swellPeriod)+" es: " +str(swellPeriodCalification))
    # print("La puntuación de la direccion del viento " + str(windDirection)+" es: " +str(windDirectionCalification))
    # print("La puntuación de la velocidad del viento " + str(windSpeed)+" es: " +str(windSpeedCalification))
    # print("La puntuación de la marea " + str(tide)+" es: " +str(tideCalification))
    
    return calification
# nordeste/este/sureste/sur/suroeste - 2 horas subiendo hasta 2 horas antes de la plea - 1'3m a 2m de mar de fondo
def set_calification_rosamunda(swellDirection, swellHeight, swellPeriod, windSpeed, windDirection, tide):
    calification = 0
    swellCalification = 0
    swellHeightCalification = 0
    swellPeriodCalification = 0
    windSpeedCalification = 0
    windDirectionCalification = 0
    tideCalification = 0
    wind = False
    
    
    if not np.isnan(swellDirection or swellHeight or swellPeriod or windSpeed or windDirection):
        swellDir = round(swellDirection)
        swellH = round(swellHeight)
        swellP = round(swellPeriod)
        windS =  round(windSpeed)
        windD = round(windDirection)
    if np.isnan(swellDirection or swellHeight or swellPeriod or windSpeed or windDirection):
        swellDir = swellDirection
        swellH = swellHeight
        swellP = swellPeriod
        windS =  windSpeed
        windD = windDirection
    # if not np.isnan(swellDirection or swellHeight or swellPeriod or windSpeed or windDirection):
    # Swell Direction 0.5
    if swellDir in np.arange (180,360):
        if swellDir in np.arange (270,330):
            swellCalification +=1
        if swellDir in np.arange (330,360):
            swellCalification +=0.3
    if swellDir in np.arange (0,180):
        if swellDir in np.arange (0 ,30):
            swellCalification +=0.3
        if swellDir in np.arange (30,80):
            swellCalification +=0.5
        if swellDir in np.arange (90,180):
            swellCalification +=0
    
    # Swell Height 2.5
    if swellH in np.arange (0,2):
        if swellH in np.arange (0,1):
            swellHeightCalification +=0
        if swellH in np.arange (1,1.5):
            swellHeightCalification +=0.7
        if swellH in np.arange (1.5,2):
            swellHeightCalification += 1
    if swellH in np.arange (2,12):
        if swellH in np.arange (2,4):
            swellHeightCalification +=2.5
        if swellH in np.arange (4,5):
            swellHeightCalification +=2
        if swellH >=5:
            swellHeightCalification +=1
    # Swell Period 3
    if swellP in np.arange (0,10):
        swellPeriodCalification +=round(swellPeriod/10,2)
    elif swellP in np.arange (10,15):
        if swellP in np.arange (10,12):
            swellPeriodCalification +=1
        if swellP in np.arange (12,15):
            swellPeriodCalification +=2
    elif swellP >=15:
            swellPeriodCalification +=3
            
    # Wind Direction 2
    if windD in np.arange (180,360):
        if windD in np.arange (180,290):
            wind = True
            windDirectionCalification +=2
        if windD in np.arange (290,360):
            windDirectionCalification +=0.5
    if windD in np.arange (0,180):
        if windD in np.arange (0 ,120):
            windDirectionCalification +=0
        elif windD in np.arange (120,160):
            windDirectionCalification +=0.5
        elif windD in np.arange (160,180):
            windDirectionCalification +=1
    
    # Wind Speed 1
    if wind == True:
        if windS in np.arange (0,7):
            if windS in np.arange (0,3):
                windSpeedCalification +=0.3
            if windS in np.arange (3,7):
                windSpeedCalification +=1
        elif windS > 7:
            if windS in np.arange (7,11):
                windSpeedCalification +=0.8
            elif windS in np.arange (11,14):
                windSpeedCalification +=0.5
            elif windS in np.arange (14,15):
                windSpeedCalification +=0.2
            elif windS >= 15:
                windSpeedCalification +=0
                
    if wind == False:
        if windS in np.arange (0,7):
            if windS in np.arange (0,3):
                windSpeedCalification +=0.5
            if windS in np.arange (3,7):
                windSpeedCalification +=0.4
        elif windS >= 7:
            if windS in np.arange (7,11):
                windSpeedCalification +=0.3
            elif windS in np.arange (11,14):
                windSpeedCalification +=0.1
            elif windS >= 14:
                windSpeedCalification +=0
            
    # Tide 1
    if tide == "low":
        tideCalification +=0.5
    if tide == "medium-low" :
        tideCalification +=0.7
    if tide == "medium-high":
        tideCalification += 1
    if tide == "high":
        tideCalification+=0.5
    calification = tideCalification+windSpeedCalification+windDirectionCalification+swellHeightCalification+swellPeriodCalification+swellCalification
    
    # print("La puntuación del swell " + str(swellDirection)+" es: " +str(swellCalification))
    # print("La puntuación del tamaño de swell " + str(swellHeight)+" es: " +str(swellHeightCalification))
    # print("La puntuación del periodo del swell " + str(swellPeriod)+" es: " +str(swellPeriodCalification))
    # print("La puntuación de la direccion del viento " + str(windDirection)+" es: " +str(windDirectionCalification))
    # print("La puntuación de la velocidad del viento " + str(windSpeed)+" es: " +str(windSpeedCalification))
    # print("La puntuación de la marea " + str(tide)+" es: " +str(tideCalification))
    
    return calification
# este/sureste/sur/suroeste - todas las mareas (depende de los fondos) - 0'5 a 1'8m de mar de fondo (depende del mar que aguanten los fondos) 
def set_calification_valdearenas(swellDirection, swellHeight, swellPeriod, windSpeed, windDirection, tide):
    calification = 0
    swellCalification = 0
    swellHeightCalification = 0
    swellPeriodCalification = 0
    windSpeedCalification = 0
    windDirectionCalification = 0
    tideCalification = 0
    wind = False
    
    
    if not np.isnan(swellDirection or swellHeight or swellPeriod or windSpeed or windDirection):
        swellDir = round(swellDirection)
        swellH = round(swellHeight)
        swellP = round(swellPeriod)
        windS =  round(windSpeed)
        windD = round(windDirection)
    if np.isnan(swellDirection or swellHeight or swellPeriod or windSpeed or windDirection):
        swellDir = swellDirection
        swellH = swellHeight
        swellP = swellPeriod
        windS =  windSpeed
        windD = windDirection
    # if not np.isnan(swellDirection or swellHeight or swellPeriod or windSpeed or windDirection):
    # Swell Direction 0.5
    if swellDir in np.arange (180,360):
        if swellDir in np.arange (270,330):
            swellCalification +=1
        if swellDir in np.arange (330,360):
            swellCalification +=0.3
    if swellDir in np.arange (0,180):
        if swellDir in np.arange (0 ,30):
            swellCalification +=0.3
        if swellDir in np.arange (30,80):
            swellCalification +=0.5
        if swellDir in np.arange (90,180):
            swellCalification +=0
    
    # Swell Height 2.5
    if swellH in np.arange (0,2):
        if swellH in np.arange (0,1):
            swellHeightCalification +=0
        if swellH in np.arange (1,1.5):
            swellHeightCalification +=0.7
        if swellH in np.arange (1.5,2):
            swellHeightCalification += 1
    if swellH in np.arange (2,12):
        if swellH in np.arange (2,4):
            swellHeightCalification +=2.5
        if swellH in np.arange (4,5):
            swellHeightCalification +=2
        if swellH >=5:
            swellHeightCalification +=1
    # Swell Period 3
    if swellP in np.arange (0,10):
        swellPeriodCalification +=round(swellPeriod/10,2)
    elif swellP in np.arange (10,15):
        if swellP in np.arange (10,12):
            swellPeriodCalification +=1
        if swellP in np.arange (12,15):
            swellPeriodCalification +=2
    elif swellP >=15:
            swellPeriodCalification +=3
            
    # Wind Direction 2
    if windD in np.arange (180,360):
        if windD in np.arange (180,290):
            wind = True
            windDirectionCalification +=2
        if windD in np.arange (290,360):
            windDirectionCalification +=0.5
    if windD in np.arange (0,180):
        if windD in np.arange (0 ,120):
            windDirectionCalification +=0
        elif windD in np.arange (120,160):
            windDirectionCalification +=0.5
        elif windD in np.arange (160,180):
            windDirectionCalification +=1
    
    # Wind Speed 1
    if wind == True:
        if windS in np.arange (0,7):
            if windS in np.arange (0,3):
                windSpeedCalification +=0.3
            if windS in np.arange (3,7):
                windSpeedCalification +=1
        elif windS > 7:
            if windS in np.arange (7,11):
                windSpeedCalification +=0.8
            elif windS in np.arange (11,14):
                windSpeedCalification +=0.5
            elif windS in np.arange (14,15):
                windSpeedCalification +=0.2
            elif windS >= 15:
                windSpeedCalification +=0
                
    if wind == False:
        if windS in np.arange (0,7):
            if windS in np.arange (0,3):
                windSpeedCalification +=0.5
            if windS in np.arange (3,7):
                windSpeedCalification +=0.4
        elif windS >= 7:
            if windS in np.arange (7,11):
                windSpeedCalification +=0.3
            elif windS in np.arange (11,14):
                windSpeedCalification +=0.1
            elif windS >= 14:
                windSpeedCalification +=0
            
    # Tide 1
    if tide == "low":
        tideCalification +=0.5
    if tide == "medium-low" :
        tideCalification +=0.7
    if tide == "medium-high":
        tideCalification += 1
    if tide == "high":
        tideCalification+=0.5
    calification = tideCalification+windSpeedCalification+windDirectionCalification+swellHeightCalification+swellPeriodCalification+swellCalification
    
    # print("La puntuación del swell " + str(swellDirection)+" es: " +str(swellCalification))
    # print("La puntuación del tamaño de swell " + str(swellHeight)+" es: " +str(swellHeightCalification))
    # print("La puntuación del periodo del swell " + str(swellPeriod)+" es: " +str(swellPeriodCalification))
    # print("La puntuación de la direccion del viento " + str(windDirection)+" es: " +str(windDirectionCalification))
    # print("La puntuación de la velocidad del viento " + str(windSpeed)+" es: " +str(windSpeedCalification))
    # print("La puntuación de la marea " + str(tide)+" es: " +str(tideCalification))
    
    return calification
# este/sureste/sur/suroeste - todas las mareas (depende de los fondos) - 0'5 a 1'8m de mar de fondo (depende del mar que aguanten los fondos) 
def set_calification_canallave(swellDirection, swellHeight, swellPeriod, windSpeed, windDirection, tide):
    calification = 0
    swellCalification = 0
    swellHeightCalification = 0
    swellPeriodCalification = 0
    windSpeedCalification = 0
    windDirectionCalification = 0
    tideCalification = 0
    wind = False
    
    
    if not np.isnan(swellDirection or swellHeight or swellPeriod or windSpeed or windDirection):
        swellDir = round(swellDirection)
        swellH = round(swellHeight)
        swellP = round(swellPeriod)
        windS =  round(windSpeed)
        windD = round(windDirection)
    if np.isnan(swellDirection or swellHeight or swellPeriod or windSpeed or windDirection):
        swellDir = swellDirection
        swellH = swellHeight
        swellP = swellPeriod
        windS =  windSpeed
        windD = windDirection
    # if not np.isnan(swellDirection or swellHeight or swellPeriod or windSpeed or windDirection):
    # Swell Direction 0.5
    if swellDir in np.arange (180,360):
        if swellDir in np.arange (270,330):
            swellCalification +=1
        if swellDir in np.arange (330,360):
            swellCalification +=0.3
    if swellDir in np.arange (0,180):
        if swellDir in np.arange (0 ,30):
            swellCalification +=0.3
        if swellDir in np.arange (30,80):
            swellCalification +=0.5
        if swellDir in np.arange (90,180):
            swellCalification +=0
    
    # Swell Height 2.5
    if swellH in np.arange (0,2):
        if swellH in np.arange (0,1):
            swellHeightCalification +=0
        if swellH in np.arange (1,1.5):
            swellHeightCalification +=0.7
        if swellH in np.arange (1.5,2):
            swellHeightCalification += 1
    if swellH in np.arange (2,12):
        if swellH in np.arange (2,4):
            swellHeightCalification +=2.5
        if swellH in np.arange (4,5):
            swellHeightCalification +=2
        if swellH >=5:
            swellHeightCalification +=1
    # Swell Period 3
    if swellP in np.arange (0,10):
        swellPeriodCalification +=round(swellPeriod/10,2)
    elif swellP in np.arange (10,15):
        if swellP in np.arange (10,12):
            swellPeriodCalification +=1
        if swellP in np.arange (12,15):
            swellPeriodCalification +=2
    elif swellP >=15:
            swellPeriodCalification +=3
            
    # Wind Direction 2
    if windD in np.arange (180,360):
        if windD in np.arange (180,290):
            wind = True
            windDirectionCalification +=2
        if windD in np.arange (290,360):
            windDirectionCalification +=0.5
    if windD in np.arange (0,180):
        if windD in np.arange (0 ,120):
            windDirectionCalification +=0
        elif windD in np.arange (120,160):
            windDirectionCalification +=0.5
        elif windD in np.arange (160,180):
            windDirectionCalification +=1
    
    # Wind Speed 1
    if wind == True:
        if windS in np.arange (0,7):
            if windS in np.arange (0,3):
                windSpeedCalification +=0.3
            if windS in np.arange (3,7):
                windSpeedCalification +=1
        elif windS > 7:
            if windS in np.arange (7,11):
                windSpeedCalification +=0.8
            elif windS in np.arange (11,14):
                windSpeedCalification +=0.5
            elif windS in np.arange (14,15):
                windSpeedCalification +=0.2
            elif windS >= 15:
                windSpeedCalification +=0
                
    if wind == False:
        if windS in np.arange (0,7):
            if windS in np.arange (0,3):
                windSpeedCalification +=0.5
            if windS in np.arange (3,7):
                windSpeedCalification +=0.4
        elif windS >= 7:
            if windS in np.arange (7,11):
                windSpeedCalification +=0.3
            elif windS in np.arange (11,14):
                windSpeedCalification +=0.1
            elif windS >= 14:
                windSpeedCalification +=0
            
    # Tide 1
    if tide == "low":
        tideCalification +=0.5
    if tide == "medium-low" :
        tideCalification +=0.7
    if tide == "medium-high":
        tideCalification += 1
    if tide == "high":
        tideCalification+=0.5
    calification = tideCalification+windSpeedCalification+windDirectionCalification+swellHeightCalification+swellPeriodCalification+swellCalification
    
    # print("La puntuación del swell " + str(swellDirection)+" es: " +str(swellCalification))
    # print("La puntuación del tamaño de swell " + str(swellHeight)+" es: " +str(swellHeightCalification))
    # print("La puntuación del periodo del swell " + str(swellPeriod)+" es: " +str(swellPeriodCalification))
    # print("La puntuación de la direccion del viento " + str(windDirection)+" es: " +str(windDirectionCalification))
    # print("La puntuación de la velocidad del viento " + str(windSpeed)+" es: " +str(windSpeedCalification))
    # print("La puntuación de la marea " + str(tide)+" es: " +str(tideCalification))
    
    return calification
    
#  suroeste/sur/sureste/este (en loredo nordeste) - todas las mareas (depende de los fondos) - 0'8 a 1'8m de mar de fondo
def set_calification_somo(swellDirection, swellHeight, swellPeriod, windSpeed, windDirection, tide):
    calification = 0
    swellCalification = 0
    swellHeightCalification = 0
    swellPeriodCalification = 0
    windSpeedCalification = 0
    windDirectionCalification = 0
    tideCalification = 0
    wind = False
    
    
    if not np.isnan(swellDirection or swellHeight or swellPeriod or windSpeed or windDirection):
        swellDir = round(swellDirection)
        swellH = round(swellHeight)
        swellP = round(swellPeriod)
        windS =  round(windSpeed)
        windD = round(windDirection)
    if np.isnan(swellDirection or swellHeight or swellPeriod or windSpeed or windDirection):
        swellDir = swellDirection
        swellH = swellHeight
        swellP = swellPeriod
        windS =  windSpeed
        windD = windDirection
    # if not np.isnan(swellDirection or swellHeight or swellPeriod or windSpeed or windDirection):
    # Swell Direction 0.5
    if swellDir in np.arange (180,360):
        if swellDir in np.arange (270,330):
            swellCalification +=1
        if swellDir in np.arange (330,360):
            swellCalification +=0.3
    if swellDir in np.arange (0,180):
        if swellDir in np.arange (0 ,30):
            swellCalification +=0.3
        if swellDir in np.arange (30,80):
            swellCalification +=0.5
        if swellDir in np.arange (90,180):
            swellCalification +=0
    
    # Swell Height 2.5
    if swellH in np.arange (0,2):
        if swellH in np.arange (0,1):
            swellHeightCalification +=0
        if swellH in np.arange (1,1.5):
            swellHeightCalification +=0.7
        if swellH in np.arange (1.5,2):
            swellHeightCalification += 1
    if swellH in np.arange (2,12):
        if swellH in np.arange (2,4):
            swellHeightCalification +=2.5
        if swellH in np.arange (4,5):
            swellHeightCalification +=2
        if swellH >=5:
            swellHeightCalification +=1
    # Swell Period 3
    if swellP in np.arange (0,10):
        swellPeriodCalification +=round(swellPeriod/10,2)
    elif swellP in np.arange (10,15):
        if swellP in np.arange (10,12):
            swellPeriodCalification +=1
        if swellP in np.arange (12,15):
            swellPeriodCalification +=2
    elif swellP >=15:
            swellPeriodCalification +=3
            
    # Wind Direction 2
    if windD in np.arange (180,360):
        if windD in np.arange (180,290):
            wind = True
            windDirectionCalification +=2
        if windD in np.arange (290,360):
            windDirectionCalification +=0.5
    if windD in np.arange (0,180):
        if windD in np.arange (0 ,120):
            windDirectionCalification +=0
        elif windD in np.arange (120,160):
            windDirectionCalification +=0.5
        elif windD in np.arange (160,180):
            windDirectionCalification +=1
    
    # Wind Speed 1
    if wind == True:
        if windS in np.arange (0,7):
            if windS in np.arange (0,3):
                windSpeedCalification +=0.3
            if windS in np.arange (3,7):
                windSpeedCalification +=1
        elif windS > 7:
            if windS in np.arange (7,11):
                windSpeedCalification +=0.8
            elif windS in np.arange (11,14):
                windSpeedCalification +=0.5
            elif windS in np.arange (14,15):
                windSpeedCalification +=0.2
            elif windS >= 15:
                windSpeedCalification +=0
                
    if wind == False:
        if windS in np.arange (0,7):
            if windS in np.arange (0,3):
                windSpeedCalification +=0.5
            if windS in np.arange (3,7):
                windSpeedCalification +=0.4
        elif windS >= 7:
            if windS in np.arange (7,11):
                windSpeedCalification +=0.3
            elif windS in np.arange (11,14):
                windSpeedCalification +=0.1
            elif windS >= 14:
                windSpeedCalification +=0
            
    # Tide 1
    if tide == "low":
        tideCalification +=0.5
    if tide == "medium-low" :
        tideCalification +=0.7
    if tide == "medium-high":
        tideCalification += 1
    if tide == "high":
        tideCalification+=0.5
    calification = tideCalification+windSpeedCalification+windDirectionCalification+swellHeightCalification+swellPeriodCalification+swellCalification
    
    # print("La puntuación del swell " + str(swellDirection)+" es: " +str(swellCalification))
    # print("La puntuación del tamaño de swell " + str(swellHeight)+" es: " +str(swellHeightCalification))
    # print("La puntuación del periodo del swell " + str(swellPeriod)+" es: " +str(swellPeriodCalification))
    # print("La puntuación de la direccion del viento " + str(windDirection)+" es: " +str(windDirectionCalification))
    # print("La puntuación de la velocidad del viento " + str(windSpeed)+" es: " +str(windSpeedCalification))
    # print("La puntuación de la marea " + str(tide)+" es: " +str(tideCalification))
    
    return calification
    
# oeste flojo/suroeste/sur/sureste - todas las mareas ( depende de los fondos) - 1'5 a 2'5m de mar de fondo 
def set_calification_langre(swellDirection, swellHeight, swellPeriod, windSpeed, windDirection, tide):
    calification = 0
    swellCalification = 0
    swellHeightCalification = 0
    swellPeriodCalification = 0
    windSpeedCalification = 0
    windDirectionCalification = 0
    tideCalification = 0
    wind = False
    
    
    if not np.isnan(swellDirection or swellHeight or swellPeriod or windSpeed or windDirection):
        swellDir = round(swellDirection)
        swellH = round(swellHeight)
        swellP = round(swellPeriod)
        windS =  round(windSpeed)
        windD = round(windDirection)
    if np.isnan(swellDirection or swellHeight or swellPeriod or windSpeed or windDirection):
        swellDir = swellDirection
        swellH = swellHeight
        swellP = swellPeriod
        windS =  windSpeed
        windD = windDirection
    # if not np.isnan(swellDirection or swellHeight or swellPeriod or windSpeed or windDirection):
    # Swell Direction 0.5
    if swellDir in np.arange (180,360):
        if swellDir in np.arange (270,330):
            swellCalification +=1
        if swellDir in np.arange (330,360):
            swellCalification +=0.3
    if swellDir in np.arange (0,180):
        if swellDir in np.arange (0 ,30):
            swellCalification +=0.3
        if swellDir in np.arange (30,80):
            swellCalification +=0.5
        if swellDir in np.arange (90,180):
            swellCalification +=0
    
    # Swell Height 2.5
    if swellH in np.arange (0,2):
        if swellH in np.arange (0,1):
            swellHeightCalification +=0
        if swellH in np.arange (1,1.5):
            swellHeightCalification +=0.7
        if swellH in np.arange (1.5,2):
            swellHeightCalification += 1
    if swellH in np.arange (2,12):
        if swellH in np.arange (2,4):
            swellHeightCalification +=2.5
        if swellH in np.arange (4,5):
            swellHeightCalification +=2
        if swellH >=5:
            swellHeightCalification +=1
    # Swell Period 3
    if swellP in np.arange (0,10):
        swellPeriodCalification +=round(swellPeriod/10,2)
    elif swellP in np.arange (10,15):
        if swellP in np.arange (10,12):
            swellPeriodCalification +=1
        if swellP in np.arange (12,15):
            swellPeriodCalification +=2
    elif swellP >=15:
            swellPeriodCalification +=3
            
    # Wind Direction 2
    if windD in np.arange (180,360):
        if windD in np.arange (180,290):
            wind = True
            windDirectionCalification +=2
        if windD in np.arange (290,360):
            windDirectionCalification +=0.5
    if windD in np.arange (0,180):
        if windD in np.arange (0 ,120):
            windDirectionCalification +=0
        elif windD in np.arange (120,160):
            windDirectionCalification +=0.5
        elif windD in np.arange (160,180):
            windDirectionCalification +=1
    
    # Wind Speed 1
    if wind == True:
        if windS in np.arange (0,7):
            if windS in np.arange (0,3):
                windSpeedCalification +=0.3
            if windS in np.arange (3,7):
                windSpeedCalification +=1
        elif windS > 7:
            if windS in np.arange (7,11):
                windSpeedCalification +=0.8
            elif windS in np.arange (11,14):
                windSpeedCalification +=0.5
            elif windS in np.arange (14,15):
                windSpeedCalification +=0.2
            elif windS >= 15:
                windSpeedCalification +=0
                
    if wind == False:
        if windS in np.arange (0,7):
            if windS in np.arange (0,3):
                windSpeedCalification +=0.5
            if windS in np.arange (3,7):
                windSpeedCalification +=0.4
        elif windS >= 7:
            if windS in np.arange (7,11):
                windSpeedCalification +=0.3
            elif windS in np.arange (11,14):
                windSpeedCalification +=0.1
            elif windS >= 14:
                windSpeedCalification +=0
            
    # Tide 1
    if tide == "low":
        tideCalification +=0.5
    if tide == "medium-low" :
        tideCalification +=0.7
    if tide == "medium-high":
        tideCalification += 1
    if tide == "high":
        tideCalification+=0.5
    calification = tideCalification+windSpeedCalification+windDirectionCalification+swellHeightCalification+swellPeriodCalification+swellCalification
    
    # print("La puntuación del swell " + str(swellDirection)+" es: " +str(swellCalification))
    # print("La puntuación del tamaño de swell " + str(swellHeight)+" es: " +str(swellHeightCalification))
    # print("La puntuación del periodo del swell " + str(swellPeriod)+" es: " +str(swellPeriodCalification))
    # print("La puntuación de la direccion del viento " + str(windDirection)+" es: " +str(windDirectionCalification))
    # print("La puntuación de la velocidad del viento " + str(windSpeed)+" es: " +str(windSpeedCalification))
    # print("La puntuación de la marea " + str(tide)+" es: " +str(tideCalification))
    
    return calification
    
# oeste (flojo)/suroeste/sur/sureste - marea baja- 1'3 a 2m de mar de fondo 
def set_calification_usgo(swellDirection, swellHeight, swellPeriod, windSpeed, windDirection, tide):
    calification = 0
    swellCalification = 0
    swellHeightCalification = 0
    swellPeriodCalification = 0
    windSpeedCalification = 0
    windDirectionCalification = 0
    tideCalification = 0
    wind = False
    
    
    if not np.isnan(swellDirection or swellHeight or swellPeriod or windSpeed or windDirection):
        swellDir = round(swellDirection)
        swellH = round(swellHeight)
        swellP = round(swellPeriod)
        windS =  round(windSpeed)
        windD = round(windDirection)
    if np.isnan(swellDirection or swellHeight or swellPeriod or windSpeed or windDirection):
        swellDir = swellDirection
        swellH = swellHeight
        swellP = swellPeriod
        windS =  windSpeed
        windD = windDirection
    # if not np.isnan(swellDirection or swellHeight or swellPeriod or windSpeed or windDirection):
    # Swell Direction 0.5
    if swellDir in np.arange (180,360):
        if swellDir in np.arange (270,330):
            swellCalification +=1
        if swellDir in np.arange (330,360):
            swellCalification +=0.3
    if swellDir in np.arange (0,180):
        if swellDir in np.arange (0 ,30):
            swellCalification +=0.3
        if swellDir in np.arange (30,80):
            swellCalification +=0.5
        if swellDir in np.arange (90,180):
            swellCalification +=0
    
    # Swell Height 2.5
    if swellH in np.arange (0,2):
        if swellH in np.arange (0,1):
            swellHeightCalification +=0
        if swellH in np.arange (1,1.5):
            swellHeightCalification +=0.7
        if swellH in np.arange (1.5,2):
            swellHeightCalification += 1
    if swellH in np.arange (2,12):
        if swellH in np.arange (2,4):
            swellHeightCalification +=2.5
        if swellH in np.arange (4,5):
            swellHeightCalification +=2
        if swellH >=5:
            swellHeightCalification +=1
    # Swell Period 3
    if swellP in np.arange (0,10):
        swellPeriodCalification +=round(swellPeriod/10,2)
    elif swellP in np.arange (10,15):
        if swellP in np.arange (10,12):
            swellPeriodCalification +=1
        if swellP in np.arange (12,15):
            swellPeriodCalification +=2
    elif swellP >=15:
            swellPeriodCalification +=3
            
    # Wind Direction 2
    if windD in np.arange (180,360):
        if windD in np.arange (180,290):
            wind = True
            windDirectionCalification +=2
        if windD in np.arange (290,360):
            windDirectionCalification +=0.5
    if windD in np.arange (0,180):
        if windD in np.arange (0 ,120):
            windDirectionCalification +=0
        elif windD in np.arange (120,160):
            windDirectionCalification +=0.5
        elif windD in np.arange (160,180):
            windDirectionCalification +=1
    
    # Wind Speed 1
    if wind == True:
        if windS in np.arange (0,7):
            if windS in np.arange (0,3):
                windSpeedCalification +=0.3
            if windS in np.arange (3,7):
                windSpeedCalification +=1
        elif windS > 7:
            if windS in np.arange (7,11):
                windSpeedCalification +=0.8
            elif windS in np.arange (11,14):
                windSpeedCalification +=0.5
            elif windS in np.arange (14,15):
                windSpeedCalification +=0.2
            elif windS >= 15:
                windSpeedCalification +=0
                
    if wind == False:
        if windS in np.arange (0,7):
            if windS in np.arange (0,3):
                windSpeedCalification +=0.5
            if windS in np.arange (3,7):
                windSpeedCalification +=0.4
        elif windS >= 7:
            if windS in np.arange (7,11):
                windSpeedCalification +=0.3
            elif windS in np.arange (11,14):
                windSpeedCalification +=0.1
            elif windS >= 14:
                windSpeedCalification +=0
            
    # Tide 1
    if tide == "low":
        tideCalification +=0.5
    if tide == "medium-low" :
        tideCalification +=0.7
    if tide == "medium-high":
        tideCalification += 1
    if tide == "high":
        tideCalification+=0.5
    calification = tideCalification+windSpeedCalification+windDirectionCalification+swellHeightCalification+swellPeriodCalification+swellCalification
    
    # print("La puntuación del swell " + str(swellDirection)+" es: " +str(swellCalification))
    # print("La puntuación del tamaño de swell " + str(swellHeight)+" es: " +str(swellHeightCalification))
    # print("La puntuación del periodo del swell " + str(swellPeriod)+" es: " +str(swellPeriodCalification))
    # print("La puntuación de la direccion del viento " + str(windDirection)+" es: " +str(windDirectionCalification))
    # print("La puntuación de la velocidad del viento " + str(windSpeed)+" es: " +str(windSpeedCalification))
    # print("La puntuación de la marea " + str(tide)+" es: " +str(tideCalification))
    
    return calification
    
# nordeste/este/sureste/sur/suroeste - normalmente marea baja, pero puede romper en todas las mareas depende de los fondos - 0'8 a 2m de mar de fondo ( si esta epic el fondo aguanta mar) 
def set_calification_gerra(swellDirection, swellHeight, swellPeriod, windSpeed, windDirection, tide):
    calification = 0
    swellCalification = 0
    swellHeightCalification = 0
    swellPeriodCalification = 0
    windSpeedCalification = 0
    windDirectionCalification = 0
    tideCalification = 0
    wind = False
    
    
    if not np.isnan(swellDirection or swellHeight or swellPeriod or windSpeed or windDirection):
        swellDir = round(swellDirection)
        swellH = round(swellHeight)
        swellP = round(swellPeriod)
        windS =  round(windSpeed)
        windD = round(windDirection)
    if np.isnan(swellDirection or swellHeight or swellPeriod or windSpeed or windDirection):
        swellDir = swellDirection
        swellH = swellHeight
        swellP = swellPeriod
        windS =  windSpeed
        windD = windDirection
    # if not np.isnan(swellDirection or swellHeight or swellPeriod or windSpeed or windDirection):
    # Swell Direction 0.5
    if swellDir in np.arange (180,360):
        if swellDir in np.arange (270,330):
            swellCalification +=1
        if swellDir in np.arange (330,360):
            swellCalification +=0.3
    if swellDir in np.arange (0,180):
        if swellDir in np.arange (0 ,30):
            swellCalification +=0.3
        if swellDir in np.arange (30,80):
            swellCalification +=0.5
        if swellDir in np.arange (90,180):
            swellCalification +=0
    
    # Swell Height 2.5
    if swellH in np.arange (0,2):
        if swellH in np.arange (0,1):
            swellHeightCalification +=0
        if swellH in np.arange (1,1.5):
            swellHeightCalification +=0.7
        if swellH in np.arange (1.5,2):
            swellHeightCalification += 1
    if swellH in np.arange (2,12):
        if swellH in np.arange (2,4):
            swellHeightCalification +=2.5
        if swellH in np.arange (4,5):
            swellHeightCalification +=2
        if swellH >=5:
            swellHeightCalification +=1
    # Swell Period 3
    if swellP in np.arange (0,10):
        swellPeriodCalification +=round(swellPeriod/10,2)
    elif swellP in np.arange (10,15):
        if swellP in np.arange (10,12):
            swellPeriodCalification +=1
        if swellP in np.arange (12,15):
            swellPeriodCalification +=2
    elif swellP >=15:
            swellPeriodCalification +=3
            
    # Wind Direction 2
    if windD in np.arange (180,360):
        if windD in np.arange (180,290):
            wind = True
            windDirectionCalification +=2
        if windD in np.arange (290,360):
            windDirectionCalification +=0.5
    if windD in np.arange (0,180):
        if windD in np.arange (0 ,120):
            windDirectionCalification +=0
        elif windD in np.arange (120,160):
            windDirectionCalification +=0.5
        elif windD in np.arange (160,180):
            windDirectionCalification +=1
    
    # Wind Speed 1
    if wind == True:
        if windS in np.arange (0,7):
            if windS in np.arange (0,3):
                windSpeedCalification +=0.3
            if windS in np.arange (3,7):
                windSpeedCalification +=1
        elif windS > 7:
            if windS in np.arange (7,11):
                windSpeedCalification +=0.8
            elif windS in np.arange (11,14):
                windSpeedCalification +=0.5
            elif windS in np.arange (14,15):
                windSpeedCalification +=0.2
            elif windS >= 15:
                windSpeedCalification +=0
                
    if wind == False:
        if windS in np.arange (0,7):
            if windS in np.arange (0,3):
                windSpeedCalification +=0.5
            if windS in np.arange (3,7):
                windSpeedCalification +=0.4
        elif windS >= 7:
            if windS in np.arange (7,11):
                windSpeedCalification +=0.3
            elif windS in np.arange (11,14):
                windSpeedCalification +=0.1
            elif windS >= 14:
                windSpeedCalification +=0
            
    # Tide 1
    if tide == "low":
        tideCalification +=0.5
    if tide == "medium-low" :
        tideCalification +=0.7
    if tide == "medium-high":
        tideCalification += 1
    if tide == "high":
        tideCalification+=0.5
    calification = tideCalification+windSpeedCalification+windDirectionCalification+swellHeightCalification+swellPeriodCalification+swellCalification
    
    # print("La puntuación del swell " + str(swellDirection)+" es: " +str(swellCalification))
    # print("La puntuación del tamaño de swell " + str(swellHeight)+" es: " +str(swellHeightCalification))
    # print("La puntuación del periodo del swell " + str(swellPeriod)+" es: " +str(swellPeriodCalification))
    # print("La puntuación de la direccion del viento " + str(windDirection)+" es: " +str(windDirectionCalification))
    # print("La puntuación de la velocidad del viento " + str(windSpeed)+" es: " +str(windSpeedCalification))
    # print("La puntuación de la marea " + str(tide)+" es: " +str(tideCalification))
    
    return calification
    
# oeste (flojo)/suroeste/sur/sureste - marea media/baja - 1'8 a 3m de mar de fondo
def set_calification_farolillo(swellDirection, swellHeight, swellPeriod, windSpeed, windDirection, tide):
    calification = 0
    swellCalification = 0
    swellHeightCalification = 0
    swellPeriodCalification = 0
    windSpeedCalification = 0
    windDirectionCalification = 0
    tideCalification = 0
    wind = False
    
    
    if not np.isnan(swellDirection or swellHeight or swellPeriod or windSpeed or windDirection):
        swellDir = round(swellDirection)
        swellH = round(swellHeight)
        swellP = round(swellPeriod)
        windS =  round(windSpeed)
        windD = round(windDirection)
    if np.isnan(swellDirection or swellHeight or swellPeriod or windSpeed or windDirection):
        swellDir = swellDirection
        swellH = swellHeight
        swellP = swellPeriod
        windS =  windSpeed
        windD = windDirection
    # if not np.isnan(swellDirection or swellHeight or swellPeriod or windSpeed or windDirection):
    # Swell Direction 0.5
    if swellDir in np.arange (180,360):
        if swellDir in np.arange (270,330):
            swellCalification +=1
        if swellDir in np.arange (330,360):
            swellCalification +=0.3
    if swellDir in np.arange (0,180):
        if swellDir in np.arange (0 ,30):
            swellCalification +=0.3
        if swellDir in np.arange (30,80):
            swellCalification +=0.5
        if swellDir in np.arange (90,180):
            swellCalification +=0
    
    # Swell Height 2.5
    if swellH in np.arange (0,2):
        if swellH in np.arange (0,1):
            swellHeightCalification +=0
        if swellH in np.arange (1,1.5):
            swellHeightCalification +=0.7
        if swellH in np.arange (1.5,2):
            swellHeightCalification += 1
    if swellH in np.arange (2,12):
        if swellH in np.arange (2,4):
            swellHeightCalification +=2.5
        if swellH in np.arange (4,5):
            swellHeightCalification +=2
        if swellH >=5:
            swellHeightCalification +=1
    # Swell Period 3
    if swellP in np.arange (0,10):
        swellPeriodCalification +=round(swellPeriod/10,2)
    elif swellP in np.arange (10,15):
        if swellP in np.arange (10,12):
            swellPeriodCalification +=1
        if swellP in np.arange (12,15):
            swellPeriodCalification +=2
    elif swellP >=15:
            swellPeriodCalification +=3
            
    # Wind Direction 2
    if windD in np.arange (180,360):
        if windD in np.arange (180,290):
            wind = True
            windDirectionCalification +=2
        if windD in np.arange (290,360):
            windDirectionCalification +=0.5
    if windD in np.arange (0,180):
        if windD in np.arange (0 ,120):
            windDirectionCalification +=0
        elif windD in np.arange (120,160):
            windDirectionCalification +=0.5
        elif windD in np.arange (160,180):
            windDirectionCalification +=1
    
    # Wind Speed 1
    if wind == True:
        if windS in np.arange (0,7):
            if windS in np.arange (0,3):
                windSpeedCalification +=0.3
            if windS in np.arange (3,7):
                windSpeedCalification +=1
        elif windS > 7:
            if windS in np.arange (7,11):
                windSpeedCalification +=0.8
            elif windS in np.arange (11,14):
                windSpeedCalification +=0.5
            elif windS in np.arange (14,15):
                windSpeedCalification +=0.2
            elif windS >= 15:
                windSpeedCalification +=0
                
    if wind == False:
        if windS in np.arange (0,7):
            if windS in np.arange (0,3):
                windSpeedCalification +=0.5
            if windS in np.arange (3,7):
                windSpeedCalification +=0.4
        elif windS >= 7:
            if windS in np.arange (7,11):
                windSpeedCalification +=0.3
            elif windS in np.arange (11,14):
                windSpeedCalification +=0.1
            elif windS >= 14:
                windSpeedCalification +=0
            
    # Tide 1
    if tide == "low":
        tideCalification +=0.5
    if tide == "medium-low" :
        tideCalification +=0.7
    if tide == "medium-high":
        tideCalification += 1
    if tide == "high":
        tideCalification+=0.5
    calification = tideCalification+windSpeedCalification+windDirectionCalification+swellHeightCalification+swellPeriodCalification+swellCalification
    
    # print("La puntuación del swell " + str(swellDirection)+" es: " +str(swellCalification))
    # print("La puntuación del tamaño de swell " + str(swellHeight)+" es: " +str(swellHeightCalification))
    # print("La puntuación del periodo del swell " + str(swellPeriod)+" es: " +str(swellPeriodCalification))
    # print("La puntuación de la direccion del viento " + str(windDirection)+" es: " +str(windDirectionCalification))
    # print("La puntuación de la velocidad del viento " + str(windSpeed)+" es: " +str(windSpeedCalification))
    # print("La puntuación de la marea " + str(tide)+" es: " +str(tideCalification))
    
    return calification
    
# sureste/sur/suroeste - media marea/alta - 1'7 a 4m de mar de fondo
def set_calification_brusco(swellDirection, swellHeight, swellPeriod, windSpeed, windDirection, tide):
    calification = 0
    swellCalification = 0
    swellHeightCalification = 0
    swellPeriodCalification = 0
    windSpeedCalification = 0
    windDirectionCalification = 0
    tideCalification = 0
    wind = False
    
    
    if not np.isnan(swellDirection or swellHeight or swellPeriod or windSpeed or windDirection):
        swellDir = round(swellDirection)
        swellH = round(swellHeight)
        swellP = round(swellPeriod)
        windS =  round(windSpeed)
        windD = round(windDirection)
    if np.isnan(swellDirection or swellHeight or swellPeriod or windSpeed or windDirection):
        swellDir = swellDirection
        swellH = swellHeight
        swellP = swellPeriod
        windS =  windSpeed
        windD = windDirection
    # if not np.isnan(swellDirection or swellHeight or swellPeriod or windSpeed or windDirection):
    # Swell Direction 0.5
    if swellDir in np.arange (180,360):
        if swellDir in np.arange (270,330):
            swellCalification +=1
        if swellDir in np.arange (330,360):
            swellCalification +=0.3
    if swellDir in np.arange (0,180):
        if swellDir in np.arange (0 ,30):
            swellCalification +=0.3
        if swellDir in np.arange (30,80):
            swellCalification +=0.5
        if swellDir in np.arange (90,180):
            swellCalification +=0
    
    # Swell Height 2.5
    if swellH in np.arange (0,2):
        if swellH in np.arange (0,1):
            swellHeightCalification +=0
        if swellH in np.arange (1,1.5):
            swellHeightCalification +=0.7
        if swellH in np.arange (1.5,2):
            swellHeightCalification += 1
    if swellH in np.arange (2,12):
        if swellH in np.arange (2,4):
            swellHeightCalification +=2.5
        if swellH in np.arange (4,5):
            swellHeightCalification +=2
        if swellH >=5:
            swellHeightCalification +=1
    # Swell Period 3
    if swellP in np.arange (0,10):
        swellPeriodCalification +=round(swellPeriod/10,2)
    elif swellP in np.arange (10,15):
        if swellP in np.arange (10,12):
            swellPeriodCalification +=1
        if swellP in np.arange (12,15):
            swellPeriodCalification +=2
    elif swellP >=15:
            swellPeriodCalification +=3
            
    # Wind Direction 2
    if windD in np.arange (180,360):
        if windD in np.arange (180,290):
            wind = True
            windDirectionCalification +=2
        if windD in np.arange (290,360):
            windDirectionCalification +=0.5
    if windD in np.arange (0,180):
        if windD in np.arange (0 ,120):
            windDirectionCalification +=0
        elif windD in np.arange (120,160):
            windDirectionCalification +=0.5
        elif windD in np.arange (160,180):
            windDirectionCalification +=1
    
    # Wind Speed 1
    if wind == True:
        if windS in np.arange (0,7):
            if windS in np.arange (0,3):
                windSpeedCalification +=0.3
            if windS in np.arange (3,7):
                windSpeedCalification +=1
        elif windS > 7:
            if windS in np.arange (7,11):
                windSpeedCalification +=0.8
            elif windS in np.arange (11,14):
                windSpeedCalification +=0.5
            elif windS in np.arange (14,15):
                windSpeedCalification +=0.2
            elif windS >= 15:
                windSpeedCalification +=0
                
    if wind == False:
        if windS in np.arange (0,7):
            if windS in np.arange (0,3):
                windSpeedCalification +=0.5
            if windS in np.arange (3,7):
                windSpeedCalification +=0.4
        elif windS >= 7:
            if windS in np.arange (7,11):
                windSpeedCalification +=0.3
            elif windS in np.arange (11,14):
                windSpeedCalification +=0.1
            elif windS >= 14:
                windSpeedCalification +=0
            
    # Tide 1
    if tide == "low":
        tideCalification +=0.5
    if tide == "medium-low" :
        tideCalification +=0.7
    if tide == "medium-high":
        tideCalification += 1
    if tide == "high":
        tideCalification+=0.5
    calification = tideCalification+windSpeedCalification+windDirectionCalification+swellHeightCalification+swellPeriodCalification+swellCalification
    
    # print("La puntuación del swell " + str(swellDirection)+" es: " +str(swellCalification))
    # print("La puntuación del tamaño de swell " + str(swellHeight)+" es: " +str(swellHeightCalification))
    # print("La puntuación del periodo del swell " + str(swellPeriod)+" es: " +str(swellPeriodCalification))
    # print("La puntuación de la direccion del viento " + str(windDirection)+" es: " +str(windDirectionCalification))
    # print("La puntuación de la velocidad del viento " + str(windSpeed)+" es: " +str(windSpeedCalification))
    # print("La puntuación de la marea " + str(tide)+" es: " +str(tideCalification))
    
    return calification
    
# nordeste/este/sureste/sur (flojo) - hora y media subiendo la marea hasta la plea -   +1'9 m de mar de fondo
def set_calification_santamarina(swellDirection, swellHeight, swellPeriod, windSpeed, windDirection, tide):
    calification = 0
    swellCalification = 0
    swellHeightCalification = 0
    swellPeriodCalification = 0
    windSpeedCalification = 0
    windDirectionCalification = 0
    tideCalification = 0
    wind = False
    
    
    if not np.isnan(swellDirection or swellHeight or swellPeriod or windSpeed or windDirection):
        swellDir = round(swellDirection)
        swellH = round(swellHeight)
        swellP = round(swellPeriod)
        windS =  round(windSpeed)
        windD = round(windDirection)
    if np.isnan(swellDirection or swellHeight or swellPeriod or windSpeed or windDirection):
        swellDir = swellDirection
        swellH = swellHeight
        swellP = swellPeriod
        windS =  windSpeed
        windD = windDirection
    # if not np.isnan(swellDirection or swellHeight or swellPeriod or windSpeed or windDirection):
    # Swell Direction 0.5
    if swellDir in np.arange (180,360):
        if swellDir in np.arange (270,330):
            swellCalification +=1
        if swellDir in np.arange (330,360):
            swellCalification +=0.3
    if swellDir in np.arange (0,180):
        if swellDir in np.arange (0 ,30):
            swellCalification +=0.3
        if swellDir in np.arange (30,80):
            swellCalification +=0.5
        if swellDir in np.arange (90,180):
            swellCalification +=0
    
    # Swell Height 2.5
    if swellH in np.arange (0,2):
        if swellH in np.arange (0,1):
            swellHeightCalification +=0
        if swellH in np.arange (1,1.5):
            swellHeightCalification +=0.7
        if swellH in np.arange (1.5,2):
            swellHeightCalification += 1
    if swellH in np.arange (2,12):
        if swellH in np.arange (2,4):
            swellHeightCalification +=2.5
        if swellH in np.arange (4,5):
            swellHeightCalification +=2
        if swellH >=5:
            swellHeightCalification +=1
    # Swell Period 3
    if swellP in np.arange (0,10):
        swellPeriodCalification +=round(swellPeriod/10,2)
    elif swellP in np.arange (10,15):
        if swellP in np.arange (10,12):
            swellPeriodCalification +=1
        if swellP in np.arange (12,15):
            swellPeriodCalification +=2
    elif swellP >=15:
            swellPeriodCalification +=3
            
    # Wind Direction 2
    if windD in np.arange (180,360):
        if windD in np.arange (180,290):
            wind = True
            windDirectionCalification +=2
        if windD in np.arange (290,360):
            windDirectionCalification +=0.5
    if windD in np.arange (0,180):
        if windD in np.arange (0 ,120):
            windDirectionCalification +=0
        elif windD in np.arange (120,160):
            windDirectionCalification +=0.5
        elif windD in np.arange (160,180):
            windDirectionCalification +=1
    
    # Wind Speed 1
    if wind == True:
        if windS in np.arange (0,7):
            if windS in np.arange (0,3):
                windSpeedCalification +=0.3
            if windS in np.arange (3,7):
                windSpeedCalification +=1
        elif windS > 7:
            if windS in np.arange (7,11):
                windSpeedCalification +=0.8
            elif windS in np.arange (11,14):
                windSpeedCalification +=0.5
            elif windS in np.arange (14,15):
                windSpeedCalification +=0.2
            elif windS >= 15:
                windSpeedCalification +=0
                
    if wind == False:
        if windS in np.arange (0,7):
            if windS in np.arange (0,3):
                windSpeedCalification +=0.5
            if windS in np.arange (3,7):
                windSpeedCalification +=0.4
        elif windS >= 7:
            if windS in np.arange (7,11):
                windSpeedCalification +=0.3
            elif windS in np.arange (11,14):
                windSpeedCalification +=0.1
            elif windS >= 14:
                windSpeedCalification +=0
            
    # Tide 1
    if tide == "low":
        tideCalification +=0.5
    if tide == "medium-low" :
        tideCalification +=0.7
    if tide == "medium-high":
        tideCalification += 1
    if tide == "high":
        tideCalification+=0.5
    calification = tideCalification+windSpeedCalification+windDirectionCalification+swellHeightCalification+swellPeriodCalification+swellCalification
    
    # print("La puntuación del swell " + str(swellDirection)+" es: " +str(swellCalification))
    # print("La puntuación del tamaño de swell " + str(swellHeight)+" es: " +str(swellHeightCalification))
    # print("La puntuación del periodo del swell " + str(swellPeriod)+" es: " +str(swellPeriodCalification))
    # print("La puntuación de la direccion del viento " + str(windDirection)+" es: " +str(windDirectionCalification))
    # print("La puntuación de la velocidad del viento " + str(windSpeed)+" es: " +str(windSpeedCalification))
    # print("La puntuación de la marea " + str(tide)+" es: " +str(tideCalification))
    
    return calification
    
def set_calification_fortaleza(swellDirection, swellHeight, swellPeriod, windSpeed, windDirection, tide):
    calification = 0
    swellCalification = 0
    swellHeightCalification = 0
    swellPeriodCalification = 0
    windSpeedCalification = 0
    windDirectionCalification = 0
    tideCalification = 0
    wind = False
    
    
    if not np.isnan(swellDirection or swellHeight or swellPeriod or windSpeed or windDirection):
        swellDir = round(swellDirection)
        swellH = round(swellHeight)
        swellP = round(swellPeriod)
        windS =  round(windSpeed)
        windD = round(windDirection)
    if np.isnan(swellDirection or swellHeight or swellPeriod or windSpeed or windDirection):
        swellDir = swellDirection
        swellH = swellHeight
        swellP = swellPeriod
        windS =  windSpeed
        windD = windDirection
    # if not np.isnan(swellDirection or swellHeight or swellPeriod or windSpeed or windDirection):
    # Swell Direction 0.5
    if swellDir in np.arange (180,360):
        if swellDir in np.arange (270,330):
            swellCalification +=1
        if swellDir in np.arange (330,360):
            swellCalification +=0.3
    if swellDir in np.arange (0,180):
        if swellDir in np.arange (0 ,30):
            swellCalification +=0.3
        if swellDir in np.arange (30,80):
            swellCalification +=0.5
        if swellDir in np.arange (90,180):
            swellCalification +=0
    
    # Swell Height 2.5
    if swellH in np.arange (0,2):
        if swellH in np.arange (0,1):
            swellHeightCalification +=0
        if swellH in np.arange (1,1.5):
            swellHeightCalification +=0.7
        if swellH in np.arange (1.5,2):
            swellHeightCalification += 1
    if swellH in np.arange (2,12):
        if swellH in np.arange (2,4):
            swellHeightCalification +=2.5
        if swellH in np.arange (4,5):
            swellHeightCalification +=2
        if swellH >=5:
            swellHeightCalification +=1
    # Swell Period 3
    if swellP in np.arange (0,10):
        swellPeriodCalification +=round(swellPeriod/10,2)
    elif swellP in np.arange (10,15):
        if swellP in np.arange (10,12):
            swellPeriodCalification +=1
        if swellP in np.arange (12,15):
            swellPeriodCalification +=2
    elif swellP >=15:
            swellPeriodCalification +=3
            
    # Wind Direction 2
    if windD in np.arange (180,360):
        if windD in np.arange (180,290):
            wind = True
            windDirectionCalification +=2
        if windD in np.arange (290,360):
            windDirectionCalification +=0.5
    if windD in np.arange (0,180):
        if windD in np.arange (0 ,120):
            windDirectionCalification +=0
        elif windD in np.arange (120,160):
            windDirectionCalification +=0.5
        elif windD in np.arange (160,180):
            windDirectionCalification +=1
    
    # Wind Speed 1
    if wind == True:
        if windS in np.arange (0,7):
            if windS in np.arange (0,3):
                windSpeedCalification +=0.3
            if windS in np.arange (3,7):
                windSpeedCalification +=1
        elif windS > 7:
            if windS in np.arange (7,11):
                windSpeedCalification +=0.8
            elif windS in np.arange (11,14):
                windSpeedCalification +=0.5
            elif windS in np.arange (14,15):
                windSpeedCalification +=0.2
            elif windS >= 15:
                windSpeedCalification +=0
                
    if wind == False:
        if windS in np.arange (0,7):
            if windS in np.arange (0,3):
                windSpeedCalification +=0.5
            if windS in np.arange (3,7):
                windSpeedCalification +=0.4
        elif windS >= 7:
            if windS in np.arange (7,11):
                windSpeedCalification +=0.3
            elif windS in np.arange (11,14):
                windSpeedCalification +=0.1
            elif windS >= 14:
                windSpeedCalification +=0
            
    # Tide 1
    if tide == "low":
        tideCalification +=0.5
    if tide == "medium-low" :
        tideCalification +=0.7
    if tide == "medium-high":
        tideCalification += 1
    if tide == "high":
        tideCalification+=0.5
    calification = tideCalification+windSpeedCalification+windDirectionCalification+swellHeightCalification+swellPeriodCalification+swellCalification
    
    # print("La puntuación del swell " + str(swellDirection)+" es: " +str(swellCalification))
    # print("La puntuación del tamaño de swell " + str(swellHeight)+" es: " +str(swellHeightCalification))
    # print("La puntuación del periodo del swell " + str(swellPeriod)+" es: " +str(swellPeriodCalification))
    # print("La puntuación de la direccion del viento " + str(windDirection)+" es: " +str(windDirectionCalification))
    # print("La puntuación de la velocidad del viento " + str(windSpeed)+" es: " +str(windSpeedCalification))
    # print("La puntuación de la marea " + str(tide)+" es: " +str(tideCalification))
    
    return calification
    
def set_calification_laredo(swellDirection, swellHeight, swellPeriod, windSpeed, windDirection, tide):
    calification = 0
    swellCalification = 0
    swellHeightCalification = 0
    swellPeriodCalification = 0
    windSpeedCalification = 0
    windDirectionCalification = 0
    tideCalification = 0
    wind = False
    
    
    if not np.isnan(swellDirection or swellHeight or swellPeriod or windSpeed or windDirection):
        swellDir = round(swellDirection)
        swellH = round(swellHeight)
        swellP = round(swellPeriod)
        windS =  round(windSpeed)
        windD = round(windDirection)
    if np.isnan(swellDirection or swellHeight or swellPeriod or windSpeed or windDirection):
        swellDir = swellDirection
        swellH = swellHeight
        swellP = swellPeriod
        windS =  windSpeed
        windD = windDirection
    # if not np.isnan(swellDirection or swellHeight or swellPeriod or windSpeed or windDirection):
    # Swell Direction 0.5
    if swellDir in np.arange (180,360):
        if swellDir in np.arange (270,330):
            swellCalification +=1
        if swellDir in np.arange (330,360):
            swellCalification +=0.3
    if swellDir in np.arange (0,180):
        if swellDir in np.arange (0 ,30):
            swellCalification +=0.3
        if swellDir in np.arange (30,80):
            swellCalification +=0.5
        if swellDir in np.arange (90,180):
            swellCalification +=0
    
    # Swell Height 2.5
    if swellH in np.arange (0,2):
        if swellH in np.arange (0,1):
            swellHeightCalification +=0
        if swellH in np.arange (1,1.5):
            swellHeightCalification +=0.7
        if swellH in np.arange (1.5,2):
            swellHeightCalification += 1
    if swellH in np.arange (2,12):
        if swellH in np.arange (2,4):
            swellHeightCalification +=2.5
        if swellH in np.arange (4,5):
            swellHeightCalification +=2
        if swellH >=5:
            swellHeightCalification +=1
    # Swell Period 3
    if swellP in np.arange (0,10):
        swellPeriodCalification +=round(swellPeriod/10,2)
    elif swellP in np.arange (10,15):
        if swellP in np.arange (10,12):
            swellPeriodCalification +=1
        if swellP in np.arange (12,15):
            swellPeriodCalification +=2
    elif swellP >=15:
            swellPeriodCalification +=3
            
    # Wind Direction 2
    if windD in np.arange (180,360):
        if windD in np.arange (180,290):
            wind = True
            windDirectionCalification +=2
        if windD in np.arange (290,360):
            windDirectionCalification +=0.5
    if windD in np.arange (0,180):
        if windD in np.arange (0 ,120):
            windDirectionCalification +=0
        elif windD in np.arange (120,160):
            windDirectionCalification +=0.5
        elif windD in np.arange (160,180):
            windDirectionCalification +=1
    
    # Wind Speed 1
    if wind == True:
        if windS in np.arange (0,7):
            if windS in np.arange (0,3):
                windSpeedCalification +=0.3
            if windS in np.arange (3,7):
                windSpeedCalification +=1
        elif windS > 7:
            if windS in np.arange (7,11):
                windSpeedCalification +=0.8
            elif windS in np.arange (11,14):
                windSpeedCalification +=0.5
            elif windS in np.arange (14,15):
                windSpeedCalification +=0.2
            elif windS >= 15:
                windSpeedCalification +=0
                
    if wind == False:
        if windS in np.arange (0,7):
            if windS in np.arange (0,3):
                windSpeedCalification +=0.5
            if windS in np.arange (3,7):
                windSpeedCalification +=0.4
        elif windS >= 7:
            if windS in np.arange (7,11):
                windSpeedCalification +=0.3
            elif windS in np.arange (11,14):
                windSpeedCalification +=0.1
            elif windS >= 14:
                windSpeedCalification +=0
            
    # Tide 1
    if tide == "low":
        tideCalification +=0.5
    if tide == "medium-low" :
        tideCalification +=0.7
    if tide == "medium-high":
        tideCalification += 1
    if tide == "high":
        tideCalification+=0.5
    calification = tideCalification+windSpeedCalification+windDirectionCalification+swellHeightCalification+swellPeriodCalification+swellCalification
    
    # print("La puntuación del swell " + str(swellDirection)+" es: " +str(swellCalification))
    # print("La puntuación del tamaño de swell " + str(swellHeight)+" es: " +str(swellHeightCalification))
    # print("La puntuación del periodo del swell " + str(swellPeriod)+" es: " +str(swellPeriodCalification))
    # print("La puntuación de la direccion del viento " + str(windDirection)+" es: " +str(windDirectionCalification))
    # print("La puntuación de la velocidad del viento " + str(windSpeed)+" es: " +str(windSpeedCalification))
    # print("La puntuación de la marea " + str(tide)+" es: " +str(tideCalification))
    
    return calification

df = df = pd.read_csv(new_path+"/"+file_name[0]+".csv")
def set_all_califications(csv_file):
    for i in range(len(csv_file)):
        # print (csv_file['sardinero_uno'][i])
        csv_file['sardinero_uno'][i] = set_calification_sardinero_uno(csv_file.loc[i,'swellDirection'],csv_file.loc[i,'swellHeight'],csv_file.loc[i,'swellPeriod'],csv_file.loc[i,'windSpeed'],csv_file.loc[i,'windDirection'],csv_file.loc[i,'tide'])
        csv_file['sardinero_dos'][i] = set_calification_sardinero_uno(csv_file.loc[i,'swellDirection'],csv_file.loc[i,'swellHeight'],csv_file.loc[i,'swellPeriod'],csv_file.loc[i,'windSpeed'],csv_file.loc[i,'windDirection'],csv_file.loc[i,'tide'])
        csv_file['mataleñas'][i] = set_calification_sardinero_uno(csv_file.loc[i,'swellDirection'],csv_file.loc[i,'swellHeight'],csv_file.loc[i,'swellPeriod'],csv_file.loc[i,'windSpeed'],csv_file.loc[i,'windDirection'],csv_file.loc[i,'tide'])
        csv_file['cañones'][i] = set_calification_sardinero_uno(csv_file.loc[i,'swellDirection'],csv_file.loc[i,'swellHeight'],csv_file.loc[i,'swellPeriod'],csv_file.loc[i,'windSpeed'],csv_file.loc[i,'windDirection'],csv_file.loc[i,'tide'])
        csv_file['rosamunda'][i] = set_calification_sardinero_uno(csv_file.loc[i,'swellDirection'],csv_file.loc[i,'swellHeight'],csv_file.loc[i,'swellPeriod'],csv_file.loc[i,'windSpeed'],csv_file.loc[i,'windDirection'],csv_file.loc[i,'tide'])
        csv_file['valdearenas'][i] = set_calification_sardinero_uno(csv_file.loc[i,'swellDirection'],csv_file.loc[i,'swellHeight'],csv_file.loc[i,'swellPeriod'],csv_file.loc[i,'windSpeed'],csv_file.loc[i,'windDirection'],csv_file.loc[i,'tide'])
        csv_file['canallave'][i] = set_calification_sardinero_uno(csv_file.loc[i,'swellDirection'],csv_file.loc[i,'swellHeight'],csv_file.loc[i,'swellPeriod'],csv_file.loc[i,'windSpeed'],csv_file.loc[i,'windDirection'],csv_file.loc[i,'tide'])
        csv_file['somo'][i] = set_calification_sardinero_uno(csv_file.loc[i,'swellDirection'],csv_file.loc[i,'swellHeight'],csv_file.loc[i,'swellPeriod'],csv_file.loc[i,'windSpeed'],csv_file.loc[i,'windDirection'],csv_file.loc[i,'tide'])
        csv_file['langre'][i] = set_calification_sardinero_uno(csv_file.loc[i,'swellDirection'],csv_file.loc[i,'swellHeight'],csv_file.loc[i,'swellPeriod'],csv_file.loc[i,'windSpeed'],csv_file.loc[i,'windDirection'],csv_file.loc[i,'tide'])
        csv_file['usgo'][i] = set_calification_sardinero_uno(csv_file.loc[i,'swellDirection'],csv_file.loc[i,'swellHeight'],csv_file.loc[i,'swellPeriod'],csv_file.loc[i,'windSpeed'],csv_file.loc[i,'windDirection'],csv_file.loc[i,'tide'])
        csv_file['gerra'][i] = set_calification_sardinero_uno(csv_file.loc[i,'swellDirection'],csv_file.loc[i,'swellHeight'],csv_file.loc[i,'swellPeriod'],csv_file.loc[i,'windSpeed'],csv_file.loc[i,'windDirection'],csv_file.loc[i,'tide'])
        csv_file['farolillo'][i] = set_calification_sardinero_uno(csv_file.loc[i,'swellDirection'],csv_file.loc[i,'swellHeight'],csv_file.loc[i,'swellPeriod'],csv_file.loc[i,'windSpeed'],csv_file.loc[i,'windDirection'],csv_file.loc[i,'tide'])
        csv_file['brusco'][i] = set_calification_sardinero_uno(csv_file.loc[i,'swellDirection'],csv_file.loc[i,'swellHeight'],csv_file.loc[i,'swellPeriod'],csv_file.loc[i,'windSpeed'],csv_file.loc[i,'windDirection'],csv_file.loc[i,'tide'])
        csv_file['santamarina'][i] = set_calification_sardinero_uno(csv_file.loc[i,'swellDirection'],csv_file.loc[i,'swellHeight'],csv_file.loc[i,'swellPeriod'],csv_file.loc[i,'windSpeed'],csv_file.loc[i,'windDirection'],csv_file.loc[i,'tide'])
        csv_file['fortaleza'][i] = set_calification_sardinero_uno(csv_file.loc[i,'swellDirection'],csv_file.loc[i,'swellHeight'],csv_file.loc[i,'swellPeriod'],csv_file.loc[i,'windSpeed'],csv_file.loc[i,'windDirection'],csv_file.loc[i,'tide'])
        csv_file['laredo'][i] = set_calification_sardinero_uno(csv_file.loc[i,'swellDirection'],csv_file.loc[i,'swellHeight'],csv_file.loc[i,'swellPeriod'],csv_file.loc[i,'windSpeed'],csv_file.loc[i,'windDirection'],csv_file.loc[i,'tide'])
        
        # set_calification_sardinero_uno(row['swellDirection'],row['swellHeight'],row['swellPeriod'],row['windSpeed'],row['windDirection'],row['tide'])

set_all_califications(df)