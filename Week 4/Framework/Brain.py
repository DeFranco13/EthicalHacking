import os
import json
from rich import print
from tqdm import tqdm
from time import sleep
import multiprocessing

dirbusterState = ""
dataScanState = ""

def line():
    print("=" * os.get_terminal_size().columns)

def ReadScans():
    pass
def StartScans():

    def Dirbuster():
        pass
    def DataScan():
        pass

    def Bar():
        with tqdm(total=100, desc="Scan 1") as pbar:
            for i in range(100):
                pbar.update(1)
                sleep(0.2)

    process1 = multiprocessing.Process(target=Dirbuster)
    process2 = multiprocessing.Process(target=DataScan)
    process3 = multiprocessing.Process(target=Bar)


    
    process1.start()
    process2.start()

    process2.join()  # Wait for the 'test' function to complete first
    process1.join()

    print("Both functions have completed.")