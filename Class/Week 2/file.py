from rich import print
import nmap
import sys
import requests
import socket
import json
import os
import server


# =====
# Dit script is de basis voor de les voorbeelden toe te passen
#
# Vars:
# =====

target = str(sys.argv[1])
ports = [21, 22, 80, 139, 443, 8080]
headerBool = True
data = []


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

data.append(dataIP)
data.append(dataScanningUpdate)

print("Ports...")
for port in ports:
    portscan = scan_v.scan(target, str(port))
    dataPort = f"Poort: {port} is " + portscan["scan"][list(portscan["scan"])[0]]["tcp"][port]["state"]

    data.append(dataPort)

dataServer = f"Host: {target} is", portscan["scan"][list(portscan["scan"])[0]]["status"]["state"]
data.append(dataServer)



# =====
# Location Scan for Host
# =====

print("Geolocating...")
dataIn = "\nHost gegevens:\n"
data.append(dataIn)

request_twee = requests.get("https://ipinfo.io/" + host_ip + "/json")
response = json.loads(request_twee.text)

dataLocation = "Locatie: " + response["loc"]
dataRegio = "Regie: " + response["region"]
dataCity = "Stad: " + response["city"]
dataCountry = "Land: " + response["country"]

data.append(dataLocation)
data.append(dataRegio)
data.append(dataCity)
data.append(dataCountry)

server.serverSock.run(data)

print("Done...!")
