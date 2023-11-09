import os
import json
from rich import print
from time import sleep
from tqdm import tqdm
import threading
import Scans.Scan4data as ScanData
import Framework.LoadSettings as Settings

website = ""
data_json_data = "Output/FoundData.json"



def line():
    print(f"\n")
    print("=" * os.get_terminal_size().columns)
    print(f"\n")   

def Bar():
     with tqdm(total=100, desc=f"Scanning {website}") as pbar:
            for i in range(100):
                pbar.update(1)
                sleep(2)
def DataScan():
    ScanData.Start(website)
    data = ScanData.getData()
    with open(data_json_data, "w") as jdata:
        json.dump(data , jdata, indent=2)

def StartScans():
    if Settings.scanState == True:
        thread1 = threading.Thread(target=DataScan)
        thread2 = threading.Thread(target=Bar)
        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()
        
    line()
    print("Scans done!")
    line()
if __name__ == "__main__":
    StartScans()
    
