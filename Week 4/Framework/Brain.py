import os
import json
from rich import print
from tqdm import tqdm
from time import sleep
import multiprocessing
import Scans.Scan4data 


website = ""
scan = 0
json_path = "Framework/settings.json"

def line():
    print("=" * os.get_terminal_size().columns)

def ReadScans():
    global dataScanState

    with open(json_path, "r") as json_file:
        data = json.load(json_file)

    dataScanState = data.get("DataScan", "")
    
def StartScans():
    def Bar():
        if scan == 1:
            with tqdm(total=100, desc="Data Scan") as pbar:
                for i in range(100):
                    pbar.update(1)
                    sleep(0.2)
        if scan == 2:
            with tqdm(total=100, desc="Dirbuster Scan") as pbar:
                for i in range(100):
                    pbar.update(1)
                    sleep(0.2)

    Scans.Scan4data.Start(website)