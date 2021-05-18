import pandas as pd
import numpy as np
import os
import config

path = config.csv_history_path
new_path = os.path.dirname(path)
file_name = os.path.splitext(os.path.basename(path))

def convert_excel_to_csv(path):
    read_file = pd.read_excel (path)
    read_file.to_csv (new_path+"/"+file_name[0]+".csv", index = None, header=True)
# convert_excel_to_csv(path)

df = pd.read_csv(new_path+"/"+file_name[0]+".csv")

def add_spots(csv_file):
    csv_file["sardinero_uno"] = ""
    csv_file["sardinero_dos"] = ""
    csv_file["mataleñas"] = ""
    csv_file["cañones"] = ""
    csv_file["rosamunda"] = ""
    csv_file["valdearenas"] = ""
    csv_file["canallave"] = ""
    csv_file["somo"] = ""
    csv_file["langre"] = ""
    csv_file["usgo"] = ""
    csv_file["gerra"] = ""
    csv_file["farolillo"] = ""
    csv_file["brusco"] = ""
    csv_file["santamarina"] = ""
    csv_file["fortaleza"] = ""
    csv_file["laredo"] = ""
    
    csv_file.to_csv (new_path+"/"+file_name[0]+".csv", index = None, header=True)

def calculate_tides(csv_file):
    tides = csv_file["tide"]
    counter = 0
    tide_counter = 0
    for tide in tides.values:
        if(tide =="high"):
            index = counter-tide_counter
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
            tide_counter = 0
            counter+=1
            continue
            
        if(tide == "low"):
            index = counter-tide_counter
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
            tide_counter = 0
            counter+=1
            continue
        
        counter+=1
        tide_counter+=1
        
    csv_file.to_csv (new_path+"/"+file_name[0]+".csv", index = None, header=True)

calculate_tides(df)