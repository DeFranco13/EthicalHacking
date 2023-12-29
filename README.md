# Ethical Hacking Project
=======================================================================================================
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

## IP Host

## Poorten

## DNS

## Geolocatie

## PEM

## Certificaten

## Directory

## Robot.txt

## Services

## Access points

## GSM nummer

## Handshake Access Points

## Deauthing Access Points

## Apparaten binnen netwerk

## Bruteforce SSH login

## Bruteforce post request login

  
