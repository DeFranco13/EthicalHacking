import os
import json
from rich import print
from tqdm import tqdm
import Scans.Scan4data 
import Framework.LoadSettings as Settings

website = ""
data_json_data = "Ouput/FoundData.json"

def line():
    print(f"\n")
    print("=" * os.get_terminal_size().columns)
    print(f"\n")   
def StartScans():

    if Settings.scanState == True:
        print("good")
        # Scans.Scan4data.Start(website)
        # data = Scans.Scan4data.getData()
        # with open(data_json_data, "w") as jdata:
        #     json.dump(data , jdata, indent=2)