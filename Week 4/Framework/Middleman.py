import Framework.Brain as Brain
import Framework.LoadSettings as Settings
import os

def Intro():
    os.system('cls' if os.name == 'nt' else 'clear')
    Brain.line()
    print(f"\nWelcome to the Pentest Framework")
    print(f"\nThis framework has been build to run several scripts with time display, to enable or disable script edit them in the json file!")
    print("Only use this script on websites with permission!")
    print(f"Feel free to experiment with this script!\n")
    Brain.line()
def LoadSettings():
    loader = Settings.SettingsLoader()
    settings = loader.load_settings()
    print(" ")
    Brain.line()
def StartProject(website):
    Intro()
    LoadSettings()
    Brain.website = website
    print(f"\nScans will start on \" {Brain.website} \"!\n")
    Brain.line()
    Brain.StartScans()

