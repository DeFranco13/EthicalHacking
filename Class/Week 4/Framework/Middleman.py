import Framework.Brain as Brain
import Framework.LoadSettings as Settings
import os

def Intro():
    os.system('cls' if os.name == 'nt' else 'clear')
    Brain.line()
    print(f"Welcome to the Pentest Framework")
    print(f"\nThis framework has been build to run several scripts with time display, to enable or disable script edit them in the json file!")
    print("Only use this script on websites with permission!")
    print(f"Feel free to experiment with this script!")
    print(f"\nPress enter tot continue...")
    Brain.line()
    a = input("")
    os.system('cls' if os.name == 'nt' else 'clear')

def LoadSettings():
    loader = Settings.load_settings()
    print(" ")
    
def StartProject(website):
    Brain.website = website
    Intro()
    LoadSettings()
    Brain.StartScans()

