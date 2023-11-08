import json
from time import sleep
from tqdm import tqdm

class SettingsLoader:
    def __init__(self, json_path="Framework/settings.json"):
        self.json_path = json_path

    def load_settings(self):
        print(" ")
        with tqdm(total=100, desc="Loading settings") as pbar:
            for i in range(100):
                pbar.update(1)
                sleep(0.12)

        
        with open(self.json_path, "r") as json_file:
            data = json.load(json_file)
            dataScanState = data.get("DataScan", "")
            return dataScanState

