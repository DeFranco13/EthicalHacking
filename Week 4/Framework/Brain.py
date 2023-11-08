import os
import json
from rich import print
from tqdm import tqdm
import Scans.Scan4data 

website = ""

def line():
    print("=" * os.get_terminal_size().columns)
    
def StartScans():
    Scans.Scan4data.Start(website)
    data = Scans.Scan4data.getData()

    for i in data:
        print(i)