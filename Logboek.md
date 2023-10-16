# Logboek Ethical Hacking
### Fransen Jordi 3CSC1

## Onderwerpen
- Ping
- Nmap
- Geolocator
- Rich module
- Headers
- Socker Client en Server
- Scapy

## Github

https://github.com/DeFranco13/EthicalHacking

## Week 1

Tijdens de eerste les hebben we verschillende python scripts bekeken en onderzocht wa deze doen. We hebben namelijk verschillende scripts bekeken die actieve en passieve scans uitvoeren op een netwerk. Deze modules zijn de basis voor een werkend framework die ons in de toekomst kan helpen in de  Cyber wereld. 

Om de bekeken modules beter te begrijpen heb ik de geziende scripts gecombineerd in 1 script en heb verder naar een dns module gezocht. Het lijkt me handig om een natwerk in te geven en dan een overzicht van alles subdomeins te krijgen. Het framework waaraan we een jaar gaan werken is ons project voor dit vak dus we gaan zelf enorm veel moeten onderzoeken en testen. 

## Week 2

We hebben een voorbeeld demo gekregen voor het opstellen van een Socker server over TCP, dit is een voorbeeld voor een 1 op 1 encrypted communicatie tussen 2 endpoints ( client en server ). Dit kan je lokaal of over het netwerk laten communiceren. Het voordeel is dat je gerichte communicatie kan delen over het netwerk. 

Scapy is een tool dat wordt gebruikt voor het analyseren van een netwerk. Je kan met scapy packets onderzoeken en ook zelf packets verzenden. Dit is daarom ook een tool voor "Ethical Hacking" omdat je black hat activiteiten kan uitvoeren. In het labo hebben we het onderzocht en bekeken hoe we het kunnne toepassen maar ik ga dit momenteel nog niet toepassen in mijn framework.

Het framework kan volgende uitbreidingen bevatten: Het framework zelf wordt op een vm geplaatst die via ssh aanstuurbaar is. Met het opstarten van het framework zal er een socket worden aangemaakt op het ip die dan de data van verwerking van het script naar de client zal doorsturen door sockets. Deze socketserver zal mee in de server zitten en zal voor x aantal seconden / minuten open staan voor verbinding en adhv de client encrypte data sturen. Op de client server zal deze data gedecrypt worden en vervolgens zijn de resultaten beschikbaar op je laptop.
