from rich import print
import nmap
import sys
import requests
import socket
import json
import os

# =====
# Dit script is de basis voor de les voorbeelden toe te passen
#
# Vars:
# =====

target = str(sys.argv[1])
ports = [21, 22, 80, 139, 443, 8080]
headerBool = True


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

print(f"\nHost IP:")
host_ip = socket.gethostbyname(sys.argv[1])
print("\nHet ip-adres van " + sys.argv[1] + " is: " + host_ip + "\n")
print(f"\nPort scan: ")
scan_v = nmap.PortScanner()
print("\nScannen van ", target, "\n")
for port in ports:
    portscan = scan_v.scan(target, str(port))
    print(
        "Poort ",
        port,
        " is ",
        portscan["scan"][list(portscan["scan"])[0]]["tcp"][port]["state"],
    )
print(
    "\nHost ",
    target,
    " is ",
    portscan["scan"][list(portscan["scan"])[0]]["status"]["state"],
)
line()


# =====
# Location Scan for Host
# =====

print(f"\nHost gegevens: \n")

request_twee = requests.get("https://ipinfo.io/" + host_ip + "/json")
response = json.loads(request_twee.text)

print("Locatie: " + response["loc"])
print("Regie: " + response["region"])
print("Stad: " + response["city"])
print("Land: " + response["country"])
