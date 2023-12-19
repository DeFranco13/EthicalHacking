import shutil
import os
import json
import Pentesting.NetworkScan as NetworkScan
import Pentesting.WebsiteScan as WebsiteScan
import Pentesting.ModuleTools as Module


global startLoop 
global WebsiteLoop
WebsiteLoop = True
startLoop = True

TRED = Module.TRED
TGREEN =  Module.TGREEN
TWHITE = Module.TWHITE


#############################
#                           #
#      Website Module       #
#                           #
#############################
    
def WebsiteSettings():
    webSettings = "Pentesting/WebScan/Input/settings.json"
    with open(webSettings, "r") as file:
        data = json.load(file)
        max_key_length = max(len(key) for key in data)
        Module.line()
        print("")
        print(f"ServiceName           Status\n")
        for key, value in data.items():
            teller = "+"
            if value == False:
                print(f'[ {TGREEN}{teller}{TWHITE} ] {key.ljust(max_key_length)} : {TRED}{value}{TWHITE}')
            elif value == True:
                print(f'[ {TGREEN}{teller}{TWHITE} ] {key.ljust(max_key_length)} : {TGREEN}{value}{TWHITE}')
        print("")

def WebsiteChange():
    loop = True
    while loop:
        webSettings = "Pentesting/WebScan/Input/settings.json"
        with open(webSettings, "r") as file:
            data = json.load(file)
            max_key_length = max(len(key) for key in data)
            Module.line()
            print("")
            print(f"ServiceName           Status\n")
            teller = 1
            for key, value in data.items():   
                if value == False:
                    print(f'[ {TGREEN}{teller}{TWHITE} ] {key.ljust(max_key_length)} : {TRED}{value}{TWHITE}')
                elif value == True:
                    print(f'[ {TGREEN}{teller}{TWHITE} ] {key.ljust(max_key_length)} : {TGREEN}{value}{TWHITE}')
                teller = teller + 1
            print(f"[ {TGREEN}{teller}{TWHITE} ] Stop editing")
            print("")
            Module.line()
            keuze = int(input("What number would u like to change: "))
            Module.clean()
            if keuze > teller -1 | keuze < 0:
                Module.line()
                print("\nWrong value!\n")
            elif keuze == teller:
                loop = False
                Module.clean()
            else:
                selected_key = list(data.keys())[keuze - 1]
                data[selected_key] = not data[selected_key]
                with open(webSettings, "w") as file:
                    json.dump(data, file, indent=2)

def Website():
    while WebsiteLoop:
        WebsiteSettings()
        Module.line()
        print("\nChoose an option: \n")
        print(f"[ {TGREEN}1{TWHITE} ] Start Scan (the above scans on True will run)")
        print(f"[ {TGREEN}2{TWHITE} ] Change Services")
        print(f"[ {TGREEN}3{TWHITE} ] Return\n")
        Module.line()
        keuze = int(input("\n->: "))
        Module.clean()
        if keuze == 1:
            loop = False
            Module.clean()
            Module.line()
            print("\nGive your target url.\nFor example google.com\n")
            Module.line()
            websiteUrl = input("\n->: ")
            WebsiteScan.Start(websiteUrl)
            break

        elif keuze == 2:
            WebsiteChange()
        
        elif keuze == 3:
            break

        else:
            continue

#############################
#                           #
#      Network Module       #
#                           #
#############################

def Device_Scan():
    NetworkScan.Device_Scan()

def Wifi_scan():
    NetworkScan.Wifi_Scan()

def Handshake():
    NetworkScan.Handshake_Scan()

def Phone():
    NetworkScan.Phone_Scan()

def Deauth():
    NetworkScan.Deauth()


#############################
#                           #
#     Starting Script       #
#                           #
#############################


def Start():
    while startLoop:
        Module.clean()
        Module.line()
        print(f"""

 ____          _   ____                   _              
 |  _ \ ___  __| | / ___| _ __   __ _ _ __| |_ __ _ _ __  
 | |_) / _ \/ _` | \___ \| '_ \ / _` | '__| __/ _` | '_ \ 
 |  _ |  __| (_| |  ___) | |_) | (_| | |  | || (_| | | | |
 |_| \_\___|\__,_| |____/| .__/ \__,_|_|   \__\__,_|_| |_|
                         |_|                             

Hacking Framework v1.0  
                  
Made by {TRED}DeFranco13{TWHITE}  
          """)
        Module.line()
        print(f"""
Choose your service:    
                
[ {TGREEN}1{TWHITE} ] Website Scan
[ {TGREEN}2{TWHITE} ] Wifi Scan
[ {TGREEN}3{TWHITE} ] Phone Number Geolocation
[ {TGREEN}4{TWHITE} ] Wifi Handshake      
[ {TGREEN}5{TWHITE} ] Wifi Deauth     
[ {TGREEN}6{TWHITE} ] Device Scan                
[ {TGREEN}7{TWHITE} ] Exit                  
        """)
        Module.line()
        keuze = int(input(f"\n->: "))
        Module.clean()
        if keuze == 1:
            Website()
        elif keuze == 2:
            Wifi_scan()
        elif keuze == 3:
            Phone()
        elif keuze == 4:
            Handshake()
        elif keuze == 5:
            Deauth()
        elif keuze == 6:
            Device_Scan()
        elif keuze == 7:
            exit()
        else:
            print("Wrong value!")
              
Start()