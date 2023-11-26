import sys
import requests
import socket
import json
from rich import print

if len(sys.argv) < 2:
    print("Gebruik: " + sys.argv[0] + " <url>")
    sys.exit(1)

request = requests.get("https://" + sys.argv[1])
print("\n" + str(request.headers))

geef_host = socket.gethostbyname(sys.argv[1])
print("\nHet ip-adres van " + sys.argv[1] + " is: " + geef_host + "\n")

# ipinfo.io

request_twee = requests.get("https://ipinfo.io/" + geef_host + "/json")
response = json.loads(request_twee.text)

print("Locatie: " + response["loc"])
print("Regie: " + response["region"])
print("Stad: " + response["city"])
print("Land: " + response["country"])
