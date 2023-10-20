from rich import print
import nmap
import sys
import requests
import socket
import json
import os
import server
import dirbuster


# =====
# Dit script is de basis voor de les voorbeelden toe te passen
#
# Vars:
# =====

target = str(sys.argv[1])
ports = [21, 22, 80, 139, 443, 8080]
headerBool = True
fileData = []


# =====
# Methodes:
# =====

def line():
    print("=" * os.get_terminal_size().columns)


# =====
# Start
# =====

if len(sys.argv) < 2:
    print("Please give a valid url.")
    sys.exit(1)

print(f"Start Script\n")
line()

# =====
# Header Request
# =====
if headerBool:
    print(f"\nRequest Header: ")
    request = requests.get("https://" + sys.argv[1])
    print("\n" + str(request.headers))
    headerBool = False
    line()


# =====
# Ip, Port & DNS scan on Host
# =====

print("Scanning...")
host_ip = socket.gethostbyname(sys.argv[1])
dataIP = "\nHet ip-adres van " + sys.argv[1] + " is: " + host_ip + "\n"
scan_v = nmap.PortScanner()
dataScanningUpdate = f"Scan results from: {target}"

fileData.append(dataIP)
fileData.append(dataScanningUpdate)

print("Ports...")
for port in ports:
    portscan = scan_v.scan(target, str(port))
    dataPort = f"Poort: {port} is " + portscan["scan"][list(portscan["scan"])[0]]["tcp"][port]["state"]

    fileData.append(dataPort)

dataServer = f"Host: {target} is", portscan["scan"][list(portscan["scan"])[0]]["status"]["state"]
fileData.append(dataServer)



# =====
# Location Scan for Host
# =====

print("Geolocating...")
dataIn = "\nHost gegevens:\n"
fileData.append(dataIn)

request_twee = requests.get("https://ipinfo.io/" + host_ip + "/json")
response = json.loads(request_twee.text)

dataLocation = "Locatie: " + response["loc"]
dataRegio = "Regie: " + response["region"]
dataCity = "Stad: " + response["city"]
dataCountry = "Land: " + response["country"]

fileData.append(dataLocation)
fileData.append(dataRegio)
fileData.append(dataCity)
fileData.append(dataCountry)

dirbuster.run()
server.serverSock.run(fileData, dirbuster.ports)


print("Done...!")
