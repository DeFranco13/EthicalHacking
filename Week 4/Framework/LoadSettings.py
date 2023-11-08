import json
from time import sleep
from tqdm import tqdm

data = ""
data_json_path = "Framework/settings.json"


def LoadScan():   
     with open(data_json_path, "r") as json_file:
            data = json.load(json_file)
            dataScanState = data.get("DataScan", "")
            return dataScanState
            
def load_settings():
        print(" ")
        with tqdm(total=100, desc="Loading settings") as pbar:
            for i in range(100):
                pbar.update(1)
                sleep(0.12)
                
        global scanState
        scanState = LoadScan()
        
        

        
        

