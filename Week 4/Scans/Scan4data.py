from rich import print
import nmap
import sys
import requests
import socket
import json
import os

# =====
# Start
# =====

def Start(website):

    # =====
    # Vars:
    # =====

    global data 
    data = []
    target = website
    ports = [21, 22, 80, 139, 443, 8080]
    headerBool = True

    

# =====
# Header Request
# =====

    if headerBool:
        data.append(f"\nRequest Header: ")
        request = requests.get("https://" + website)
        data.append(f"\n {str(request.headers)}")
        headerBool = False


# =====
# Ip, Port & DNS scan on Host
# =====

    data.append(f"\nHost IP:")
    host_ip = socket.gethostbyname(website)
    data.append("\nHet ip-adres van " + website + " is: " + host_ip + "\n")
    data.append(f"\nPort scan:")
    scan_v = nmap.PortScanner()
    data.append(f"\nScannen van {target}\n")
    
    for port in ports:
        portscan = scan_v.scan(target, str(port))
        dataPort = f"Poort: {port} is " + portscan["scan"][list(portscan["scan"])[0]]["tcp"][port]["state"]
        data.append(dataPort)
    
    dataServer = f"Host: {target} is " + portscan["scan"][list(portscan["scan"])[0]]["status"]["state"]   
    data.append(dataServer)

# =====
# Location Scan for Host
# =====

    data.append("\nHost gegevens: \n")

    request_twee = requests.get("https://ipinfo.io/" + host_ip + "/json")
    response = json.loads(request_twee.text)

    data.append("Locatie: " + response["loc"])
    data.append("Regie: " + response["region"])
    data.append("Stad: " + response["city"])
    data.append("Land: " + response["country"])

def getData():
    return data
