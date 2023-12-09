import shutil
import os
import json
import Pentesting.NetworkScan as NetworkScan
import Pentesting.WebsiteScan as WebsiteScan

global startLoop 
global WebsiteLoop
global NetworkLoop
WebsiteLoop = True
NetworkLoop = True
startLoop = True

def line():
    # Get the terminal width
    terminal_width, _ = shutil.get_terminal_size()

    # Print a line of "=" characters
    print("=" * terminal_width)

def clean():
    os.system('cls' if os.name == 'nt' else 'clear')

def WebsiteSettings():
    webSettings = "Pentesting/WebScan/Input/settings.json"
    with open(webSettings, "r") as file:
        data = json.load(file)
        max_key_length = max(len(key) for key in data)
        line()
        print("")
        print(f"ServiceName           Status\n")
        for key, value in data.items():
            print(f'{key.ljust(max_key_length)} : {value}')
        print("")

def WebsiteChange():
    loop = True
    while loop:
        webSettings = "Pentesting/WebScan/Input/settings.json"
        with open(webSettings, "r") as file:
            data = json.load(file)
            max_key_length = max(len(key) for key in data)
            line()
            print("")
            print(f"ServiceName           Status\n")
            teller = 1
            for key, value in data.items():   
                print(f'{teller}) {key.ljust(max_key_length)} : {value}')
                teller = teller + 1
            print(f"{teller}) Stop editing")
            print("")
            line()
            keuze = int(input("What number would u like to change: "))
            clean()
            if keuze > teller -1 | keuze < 0:
                line()
                print("\nWrong value!\n")
            elif keuze == teller:
                loop = False
                clean()
            else:
                selected_key = list(data.keys())[keuze - 1]
                data[selected_key] = not data[selected_key]
                with open(webSettings, "w") as file:
                    json.dump(data, file, indent=2)

def Website():
    while WebsiteLoop:
        WebsiteSettings()
        line()
        print("\nChoose an option: \n")
        print("1) Start Scan (the above scans on True will run)")
        print("2) Change Services")
        print("3) Return\n")
        line()
        keuze = int(input("\n->: "))
        clean()
        if keuze == 1:
            loop = False
            clean()
            line()
            print("\nGive your target url.\nFor example google.com\n")
            line()
            websiteUrl = input("\n->: ")
            WebsiteScan.Start(websiteUrl)
            break

        elif keuze == 2:
            WebsiteChange()
        
        elif keuze == 3:
            break

        else:
            continue

def NetworkSettings():
    networkSetting = "Pentesting/Network/Input/settings.json"
    with open(networkSetting, "r") as file:
        data = json.load(file)
        max_key_length = max(len(key) for key in data)
        line()
        print("")
        print(f"ServiceName           Status\n")
        for key, value in data.items():
            print(f'{key.ljust(max_key_length)} : {value}')
        print("")

def NetworkChange():
    loop = True
    while loop:
        networkSetting = "Pentesting/Network/Input/settings.json"
        with open(networkSetting, "r") as file:
            data = json.load(file)
            max_key_length = max(len(key) for key in data)
            line()
            print("")
            print(f"ServiceName           Status\n")
            teller = 1
            for key, value in data.items():   
                print(f'{teller}) {key.ljust(max_key_length)} : {value}')
                teller = teller + 1
            print(f"{teller}) Stop editing")
            print("")
            line()
            keuze = int(input("What number would u like to change: "))
            clean()
            if keuze > teller -1 | keuze < 0:
                line()
                print("\nWrong value!\n")
            elif keuze == teller:
                loop = False
                clean()
            else:
                selected_key = list(data.keys())[keuze - 1]
                data[selected_key] = not data[selected_key]
                with open(networkSetting, "w") as file:
                    json.dump(data, file, indent=2)        

def Network():
    while NetworkLoop:
        NetworkSettings()
        line()
        print("\nChoose an option: \n")
        print("1) Start Scan (the above scans on True will run)")
        print("2) Change Services")
        print("3) Return\n")
        line()
        keuze = int(input("\n->: "))
        clean()
        if keuze == 1:
            clean()
            NetworkScan.Start()
            break

        elif keuze == 2:
            NetworkChange()
            
        elif keuze == 3:
            break
        else:
            continue

def Start():
    while startLoop:
        clean()
        line()
        print("""

 ____          _   ____                   _              
 |  _ \ ___  __| | / ___| _ __   __ _ _ __| |_ __ _ _ __  
 | |_) / _ \/ _` | \___ \| '_ \ / _` | '__| __/ _` | '_ \ 
 |  _ |  __| (_| |  ___) | |_) | (_| | |  | || (_| | | | |
 |_| \_\___|\__,_| |____/| .__/ \__,_|_|   \__\__,_|_| |_|
                         |_|                             

Hacking Framework v1.0        
          """)
        line()
        print("""
Choose your service:    
                
1) Website
2) Network    
3) Exit                  
        """)
        line()
        keuze = int(input(f"\n->: "))
        clean()
        if keuze == 1:
            Website()
        elif keuze == 2:
            Network()
        
        elif keuze == 3:
            exit()
        else:
            print("Wrong value!")
    
Start()