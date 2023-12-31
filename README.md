# Ethical Hacking Project
==================================================================================
## Inhoud:

### Gebruik van applicatie

De applicatie is zodanig opgebouwd dat je vanuit het menu een keuze kan maken van je scan / aanval. Bij de gemaakte keuze zal je bij elke optie extra gegevens moeten invullen zoals ip, url, nummer of andere dergelijke zaken. Het systeem zo dynamisch mogelijk opgesteld zodat er binnen in een module meerdere functies tegelijk zullen werken voor het process sneller te laten verlopen. Ook zal het na elke uitvoering de gebruiker terug brengen naar het begin scherm. Al de data wordt niet vertoond op de gebruiker zijn scherm maar elke module kan zijn eigen outputfiles genereren en deze plaatsen onder Pentesting/Output. Voor het gebruik van de applicatie te vereenvoudigen heb ik de optie toegevoegd om de Output folder te downloaden naar de gebruiker zijn Download zone op zijn computer. 

### Verwerkte modules:

Binnenin de tijdspannen van het project hebben we verschillende nuttige in interessante modules onderzocht en toegepast. Onderstaande modules heb ik gekozen om verder uit te werken tot een geheel.

#### Website scan
- Header request
- IP Host adres
- Poorten
- DNS
- Geolocatie
- PEM
- Certificaat
- Directory
- Robot.txt
- Services
  
#### Wifi scan
- Access Points scanner
- Gsm nummer tracking
- Handshake van Access Point
- Deauthen van Access Point
- Apparaten scan binnen in netwerk
  
#### Aanvallen
- Bruteforce SSH login
- Bruteforce Login post request

=======================================================================================================
## Applicatie

Een leerkracht op middelbaar vertelde me altijd "Elk kind heeft een naam nodig". Daarom vond ik het nodig om een toepasselijke naam te verzinnen voor het framework. Ik kwam al snel op de griekse strijder sparten, ze zijn bekend voor hun strijdkracht en ik wil dit ook vertonen binnen het project, een simpel geschreven project dat terwijl enorm krachting kan zijn.

Start commando:
`python3 RedSpartan_framework.py`

Bij het opstart van het script krijgt de gebruiker het volgende beeld te zien:
<img width="1435" alt="Screenshot 2023-12-29 at 18 26 09" src="https://github.com/DeFranco13/EthicalHacking/assets/75678058/7876f18d-fb98-459d-9937-e87657cb8a20">
De gebruiker moet de nummer ingeven van de service die hij wilt toepassen. Als de gebruiker een ongeldig nummer invoert dat wordt de app steeds weer opnieuw opgestart. De app is opgebouwd met een oneindig lopende loop, deze loop kan enkel worden stop gezet als de gebruiker voor de optie kiest voor de app uit te zetten of de gebruiker de app sluit met control+c.

## Website scan

Ik heb de modules ingedeeld, in categorieën geplaatst en verkleind om het zo gebruiksvriendelijk en makkelijk te maken voor de gebruiker. Vanaf dat de gebruiker de website scan als optie neemt krijgt hij volgende scherm te zien:
![image](https://github.com/DeFranco13/EthicalHacking/assets/75678058/8ed6b51a-fd7f-47f7-b8fb-21428d7c42e8)

Hier kan de gebruiker zijn scan opties aanpassen, of het script runnen met de gekozen opties. Ook wordt de Ouput folder steeds leeggemaakt voor het initialiseren van een nieuwe scan. Dit doet het script zodat er geen dubelle files zullen plaatsen, dit kan enkel voor foutmeldingen zorgen.

![image](https://github.com/DeFranco13/EthicalHacking/assets/75678058/fd0d69df-3efd-42e1-9dcd-be63162b564c)

Vanaf dat de gebruiker zijn scan opties gekozen heeft en hij kiest om de scans uit te voeren zullen al de scans via threading uitgevoert worden. Er is een progress bar ingesteld met de resterende tijd van de thread. Vanaf dat alle scans zijn uitgevoerd zal de gebruiker terug naar het beginscherm gestuurd worden.

Scan proces:

![image](https://github.com/DeFranco13/EthicalHacking/assets/75678058/d99ef245-5840-468a-8711-691ee2bc7a02)

Al de output wordt bijgehoude:

![image](https://github.com/DeFranco13/EthicalHacking/assets/75678058/616f6a63-88c8-445c-9168-c1725df026b9)



## Header Request

Tijdens de data scan van de host wordt er een request uitgevoerd naar de host toe. De response hiervan houden we bij en slaan we op in een bestand. Dit is een voorbeeld van een header request:

Script:

![image](https://github.com/DeFranco13/EthicalHacking/assets/75678058/bf1298ff-e921-4e0b-81c1-496565a4c59d)


Output:

![image](https://github.com/DeFranco13/EthicalHacking/assets/75678058/bffdb059-c5b9-4bc9-a623-d7dc82ebe984)


## IP Host

Tijdens de data scan zal de url die werd meegegeven gekoppeld worden aan een vast IP adres. Dit IP adres is noodzakelijk voor andere scans later in de module.

## Poorten

Voor het onderzoeken van openstaande poorten van de host hebben we zijn vast IP adres nodig. Door gebruik van Nmap kunnen we een poort scan uitvoeren op het IP adres en onderzoeken welke poorten er open staan. Deze poorten zijn enorm nuttig voor aanvallen voor te bereiden of om ze te voorkomen.

Script:

![image](https://github.com/DeFranco13/EthicalHacking/assets/75678058/1466a049-8ae8-4da4-8770-df5d6d76ff5b)


Output:

![image](https://github.com/DeFranco13/EthicalHacking/assets/75678058/da41a1c9-3243-4231-866b-0b6a5b6bcc48)


## DNS

Het onderzoeken van enkele DNS subdomeinen hebben we enkel de url nodig. Deze werd opgegeven door het initialiseren van de module. Door het gebruik van sublist3r en subprocessen scannen we de subdomeinen van de host.

Script:

![image](https://github.com/DeFranco13/EthicalHacking/assets/75678058/8b7a04b9-4d4b-4484-9c16-063b58515e5a)


Output:

![image](https://github.com/DeFranco13/EthicalHacking/assets/75678058/7bb84e9e-fa85-484b-8696-4e3254d33e65)



## Geolocatie

De locatie van de servers worden onderzocht samen met het onderzoeken van het IP adres. Dit geeft de locatie weer vanwaar de server wordt gehost. De output geeft coördinaten terug samen met het land en de stad.

Script:

![image](https://github.com/DeFranco13/EthicalHacking/assets/75678058/b609fc74-840e-4a82-a513-80a888de54a2)


Output:

![image](https://github.com/DeFranco13/EthicalHacking/assets/75678058/6628533e-f940-46bf-b903-ee60e8a856f5)


## PEM

In het script wordt er automatische scan uitgevoerd naar de url voor het ontvangen van de public key die wordt gebruikt voor het tekenen van het https certificaat. Deze sleutel heeft het script ontvangen, opgeslagen en is toegankelijk in de Output folder. De sleutel ontvangen we door het commando openSSL, dit geeft een XML bestand terug waarop wij een filter gebruiken voor enkel de PEM te ontvangen.

Script:

![image](https://github.com/DeFranco13/EthicalHacking/assets/75678058/110f624a-f578-47de-884e-d88b1772b50e)

Output:

![image](https://github.com/DeFranco13/EthicalHacking/assets/75678058/4a383378-74f8-473d-a106-89b65337edff)

## Certificaten

Het script maakt gebruikt van het commando openSSL, dit commando gaat het certificaat van de webserver opvragen, deze gegevens worden in een XML formaat terug gegeven. Dit formaat is natuurlijk niet makkelijk om te lezen. Daarom heb ik een extra module geschreven om de gekozen data hieruit te filteren en op te slaan in een CSV bestand. Dit is makkelijk leesbaar voor de gebruiker. 

SSL script:

![image](https://github.com/DeFranco13/EthicalHacking/assets/75678058/fad67eb5-b976-4310-923d-7a6f89afd330)

Filter script:

![image](https://github.com/DeFranco13/EthicalHacking/assets/75678058/40a74400-55b3-4cdc-b6d4-55a6b4b890ca)

XML output:

![image](https://github.com/DeFranco13/EthicalHacking/assets/75678058/ec07fcdf-0df2-420b-bd57-70f72e32437d)

CSV output:

![image](https://github.com/DeFranco13/EthicalHacking/assets/75678058/8b8a49c2-feed-41c7-bef0-ee99c6f59618)


In de CSV zijn er 2 lijnen beschikbaar met data, sommige vakken zijn undefined. Dit komt omdat niet al de data in hetzelfde type stond en ik heb een filtering op short en full type uitgevoert voor al de data te verzamelen. 



## Directory

Er is een module ingebouwd voor het automatisch onderzoeken voor directories van de webserver. Dit doen we door gebruik van Gobuster. Het runnen van dit commando duurt enorm lang omdat hij een medium directory lijst onderzoekt. Deze lijst is aanwezig onder WebScan en dna Tools. Het script geeft als output een bestand terug met al de gevonden paths erin vermeld!

Script:

![image](https://github.com/DeFranco13/EthicalHacking/assets/75678058/7caf1c5f-d0f5-4504-9808-8547811501e0)


## Robot.txt

Niet elke site heeft hun Robot.txt file verborgen. Toch kan deze site soms veel informatie terug geven. Daarom zal het framework ook deze file proberen terug te ontvangen. Mocht dit slagen dan genereert hij een bestand met de output van de robot file. Hiervoor maken we een simpele request naar de url met daarachter /robot.txt aan toegevoegd.

Script:

![image](https://github.com/DeFranco13/EthicalHacking/assets/75678058/f98ec328-c899-4bb2-b36d-2b0487ecef34)


Output:

![image](https://github.com/DeFranco13/EthicalHacking/assets/75678058/2893ffea-0409-475c-8841-065264fbba32)


## Services

Het leek me enrom interessant om te onderzoeken welke services en componenten er in de backend van een webserver draaien. Via Wappalyzer kunnen we dit simpel onderzoeken. Wappalyzer is niet enkel een enorm handige extension voor je browser maar het kan ook via python gebruikt worden. Het geeft een json bestand terug met daarin de informatie van de achterliggende services en hun huidige versie. 

Script:

![image](https://github.com/DeFranco13/EthicalHacking/assets/75678058/a3ee0240-5c09-4822-85ce-bc66a65bf559)


Output:

![image](https://github.com/DeFranco13/EthicalHacking/assets/75678058/a9141964-7021-4cef-9cef-6a6a21f4eeab)


## Access points

Bij het kiezen van de Wifi Scan optie zal het script al de beschikbare access points in de buurt opvragen en opslaan in een bestand. Er zijn 2 versies gemaakt voor het script: 1 voor Linux en 1 voor Darwin. Voor Linux werken we met nmcli die eenvoudig alles kan opvragen en voor Darwin werken we met airport. Beide scripts hebben sudo rechten nodig voor het ontvangen van de data. 

Script:

![image](https://github.com/DeFranco13/EthicalHacking/assets/75678058/408d062a-3a7f-43b7-b9d7-3385016af938)

![image](https://github.com/DeFranco13/EthicalHacking/assets/75678058/cf8e19d8-a855-45b1-95c8-8512f6e6ecb8)

Output:

![image](https://github.com/DeFranco13/EthicalHacking/assets/75678058/10e604ea-2b3a-46da-b45f-06068638f22b)


## GSM nummer

Met deze module kan je simpel een telefoon nummer invoeren en het script zal een locatie koppelen aan de nummer. Voor het script ethisch te houden is niet nauwkeuring maar een landelijke weergave. Hiervoor gebruiken we een API die de nummer zal onderzoeken en een output terug geeft.

Script:

![image](https://github.com/DeFranco13/EthicalHacking/assets/75678058/717cdbd5-bc03-478a-a782-f61a33f10881)


Output:

![image](https://github.com/DeFranco13/EthicalHacking/assets/75678058/c9117549-326c-4f30-b3c2-5abf07b6a5ac)


## Handshake Access Points

Script:

Niet uitgetest op een website voor ethische redenen.

## Deauthing Access Points

Script:

Niet uitgetest op een website voor ethische redenen.

## Apparaten binnen netwerk

Voor het verzamelen van apparaten binnen een netwerk gebruiken we weer Nmap, nu gebruiken we de optie -sn voor de scan uit te voeren. Het geeft een json bestand weer dat wordt opgeslagen!

Script:

![image](https://github.com/DeFranco13/EthicalHacking/assets/75678058/da5fce0f-a17c-4577-9fda-ae5b3cb80baa)


Output:

![image](https://github.com/DeFranco13/EthicalHacking/assets/75678058/bc909562-cb0a-4c44-a8a2-fe763e0f3f18)


## Bruteforce SSH login

Script:

Niet uitgetest op een website voor ethische redenen.

## Bruteforce post request login

Script:

Niet uitgetest op een website voor ethische redenen.

  
