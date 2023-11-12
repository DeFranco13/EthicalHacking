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

## Week 3

We hebben in het verleden al bekeken naar verschillende manieren van cryptografie, deze hebben we in de les herbekeken en veel ervan was herhaling. Verder heb ik aandacht besteden aan de Django modulen. Tot nu toe heb ik de server werkende gekregen en ben ik aan het overwegen om er een gui in te ontwikkelen met daarin mijn framework code zodat deze niet altijd via console moet. Verder is het wel handig en sneller om met een console te werken omdat de output toch naar bestanden toe wordt gefilterd. 

Ik heb verder nog research gedaan over wordpress mapping en bruteforcing, deze spraken mezelf niet enorm veel aan omdat het modules zijn die ik al reeds gebruik via andere commando's zoals gobuster en hydra of zelf burpsuite. Natuurlijk is wel handig om het te automatiseren in een werkend framework. Ik ga de modules nog verder evalueren en moest deze positief zijn pas ik deze toe in het framework. 

Ik heb de brute forcing toegepast in een nieuwe structuur, mijn framework ziet er momenteel uit als 1 py bestand voor het opstarten en dan 2 folders met daarin de functies die worden uitgevoerd. De eerste folder heeft als doel om alle data van een server op te halen en deze door te sturen, de 2de heeft als doel toegang te krijgen op de website. Via het start script zal deze automatisch worden uitgevoerd door de keuze van de gebruiker. 

## Week 4

In deze week heb ik de hele structuur van grond af opnieuw gemaakt. In plaats van dat je een .py file aanspreekt en die volgt alles in het script uit is er nu een main.py script dat de werking in gang zet door 9 andere python bestanden. Deze bestanden bevatten zijn zo opgesteld dat ze elkaar nodig hebben en elkaar constant gebruiken en uitlezen. Verder zijn er Input / Output folders die worden egbruikt voor het behandelen van het script. In de Input folder is er settings.json aanwezig, dit is een bestand die wordt uitgelezen en adhv de keuzes zullen er bepaalde modules worden uitgevoerd. 

De reeds aanwezige modules doen het volgende: Verzamelen van data, ip , locatie, ports, backend, certificaat gegevens. Momenteel staan er nog verschillende modules op de planning maar dit zijn al de reeds geïnstalleerde modules. De framework die we in deze tijd begint stilaan zijn structuur te krijgen en is ook simpel aan te vullen en is enorm flexibel. 