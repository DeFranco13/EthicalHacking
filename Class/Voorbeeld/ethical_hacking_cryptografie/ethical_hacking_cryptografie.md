# Ethical hacking: labo - encryptie/decryptie

## Oefening 1: versleutelen met de Caesar versleuteling

Het Caesar Cipher is een van de eenvoudigste en bekendste encryptietechnieken. Het is een soort substitutieversleuteling waarbij elke letter in de plaintext (de te versleutelen tekst) wordt 'verschoven' een bepaald aantal plaatsen verderop in het alfabet. Dit aantal plaatsen, bekend als de 'sleutel', is hetzelfde voor alle letters in de bericht. 

Bijvoorbeeld, met een verschuiving (of sleutel) van 3:
- A wordt D
- B wordt E
- C wordt F
- ... 
- Z wordt C

De algemene formule om een letter te encrypteren in de Caesar Cipher is:
\[ E_n(x) = (x + n) \mod {26} \]

Waarbij:
- \( E_n(x) \) de uitvoer is na encryptie,
- \( x \) de originele letter is (uitgedrukt als een getal, waarbij A=0, B=1, enzovoort),
- \( n \) de verschuiving (of sleutel),
- en \( \mod {26} \) de modulo-operator die ervoor zorgt dat de encryptie 'rondgaat' na Z.

De decryptie werkt op dezelfde manier, alleen gebruik je dan de tegengestelde verschuiving:
\[ D_n(x) = (x - n) \mod {26} \]

Het Caesar Cipher is zeer gemakkelijk te breken en daarom in de hedendaagse cryptografie niet meer gebruikt voor beveiligingstoepassingen, maar het wordt wel vaak aangehaald als een eenvoudig en begrijpelijk voorbeeld bij de introductie tot cryptografie.

Jouw opdracht: je schrijft een programma dat in staat is een boodschap te encrypteren met de Caesar versleuteling en de boodschap ook te decrypteren. Je hoeft geen interface te maken: werk met variabelen.
Variabelen voor boodschap, sleutel, actie: encrypteren/decrypteren.


## Oefening 2: het bruteforcen van een met de Caesar versleuteling geëncrypteerde boodschap

Jouw opdracht: je gaat een met Caesar versleuteling geëncrypteerde boodschap decrypteren. Je kent de sleutel niet. Je gaat dus voor elke mogelijke sleutel een decryptie tonen. Je logt deze naar de console. Je zal visueel snel kunnen zien welke sleutel de echte vertaalde boodschap heeft teruggegeven. En dat volstaat hier.

## Oefening 3: kolomtranspositie versleuteling

Het Caesar cipher is relatief eenvoudig te hacken. Dat heb je zelf kunnen vaststellen in de vorige opdracht. Om onze boodschappen beter te beveiligen hebben we een betere encryptie nodig. In deze oefening gaan we gebruik maken van kolomtranspositie versleuteling.

kolomtranspositie werkt als volgt:

1. De te versleutelen boodschap (plaintext) wordt horizontaal geschreven in een vastgesteld aantal kolommen. Het aantal kolommen is typisch gebaseerd op een sleutelwoord of een getal.
   
2. De boodschap wordt vervolgens verticaal uitgelezen, kolom voor kolom, om de gecodeerde boodschap (de cipher tekst) te creëren.

3. Stel, we hebben de tekst "HELLO WORLD" en we kiezen om deze in drie kolommen te schrijven:

```
    H E L
    L O W
    O R L
    D
```
Vervolgens lezen we de tekst verticaal per kolom: "HLODEORLWL".

4. Om te decrypten wordt de proces omgekeerd. De cipher tekst wordt geschreven in een aantal kolommen dat wordt bepaald door de lengte van de originele boodschap en de sleutel, en vervolgens horizontaal uitgelezen.

Merk op: hoewel de kolomtranspositie cipher veel sterker is dan eenvoudige substitutieciphers vanwege het herarrangeren van de letters, kan het nog steeds effectief worden gebroken met genoeg tekst en analyse. Het is echter een goed voorbeeld van hoe transpositie als een cryptografisch mechanisme werkt.

Jouw opdracht: schrijf een programma dat encrypteert met deze versleuteling. 

Je hoeft geen interface te maken: werk met variabelen.
Variabelen voor boodschap, sleutel.
Je logt de geëncrypteerde boodschap naar de terminal.


## Oefening 4: kolomtranspositie decryptie

Jouw opdracht: schrijf een programma dat decrypteert met deze versleuteling. 

Je hoeft geen interface te maken: werk met variabelen.
Variabelen voor boodschap, sleutel.
Je logt de gedecrypteerde boodschap naar de terminal.


## Oefening 5: encrypteren en decrypteren van bestanden

Je breidt oefeningen 3 en 4 uit (importeer hen ;-)) en zorg ervoor dat er van een bronbestand kan worden ingelezen en naar een nieuw bestand kan worden geschreven.

Je hoeft geen interface te maken: werk met variabelen.
Je logt basisinfo naar de terminal. Meet hoelang de encryptie/decryptie duurde en log naar het scherm.


## Oefening 6: detecteer of een string Nederlandse taal bevat

Op basis van een tekstbestand met Nederlandse woorden probeer je na te gaan of een string geschreven is in Nederlands of niet. Je kan deze functie testen op oefening 2 of je schrijft een extra script dat je programma werkt.

Het bestand in kwestie vind je op Digitap: woordenlijst.txt

## Oefening 7: het bruteforcen van een met de kolomtranspositie versleuteling geëncrypteerde boodschap

Voor de doorzetters ;-) Probeer nu tot slot een kolomtranspositie geëncrypteerde string te bruteforce decrypteren. Je kent uiteraard de key niet, dus je overloopt ze allemaal. Maar je probeert dmv het herkennen van het Nederlands uit oefening 6 enkel de juiste oplossing te weerhouden.

## Oefening 8: vermenigvuldigingsversleuteling

In de context van cryptografie verwijst vermenigvuldigingsversleuteling specifiek naar een soort substitutiecijfer waarbij elke letter in het bericht wordt vervangen door een andere letter. De vervanging vindt plaats volgens een vooraf bepaalde wiskundige formule, die een vermenigvuldiging bevat als centrale bewerking. Vaak wordt bij klassieke cijfers gewerkt met de numerieke equivalenten van letters (bijvoorbeeld a=0, b=1, ..., z=25) en wiskundige bewerkingen worden in een modulo stelsel uitgevoerd om binnen het alfabet te blijven. In het geval van een multiplicative cipher, wordt elk getal (dat een letter voorstelt) vermenigvuldigd met een gekozen sleutel en vervolgens gemoduleerd door de lengte van het alfabet om een nieuw getal te krijgen dat dan wordt omgezet naar een letter, resulterend in de versleutelde tekst.

- Je zoekt op hoe vermenigvuldigingsversleuteling werkt
- Welke toepassingen kent/kende dit soort versleuteling?
- Je schrijft een Python-script dat volgens deze versleuteling encrypteert en decrypteert.

### Tip: niet alle sleutels kunnen gebruikt worden

Bij het gebruik van het vermenigvuldigingscijfer voor versleuteling kunnen niet alle sleutels worden gebruikt. Een sleutel is geldig als en slechts als deze een wederzijds priemgetal is met betrekking tot het aantal gebruikte symbolen. Dus, als we een alfabet gebruiken van 26 letters, dan moet de sleutel die we kiezen voor het vermenigvuldigingscijfer een getal zijn dat geen gemeenschappelijke factoren heeft met 26, behalve 1 (dat wil zeggen, het moet copriem zijn met 26). Dit is essentieel om ervoor te zorgen dat de vermenigvuldigingsversleuteling omkeerbaar is, wat betekent dat de originele tekst altijd kan worden hersteld door te ontcijferen. In de context van een alfabet van 26 letters, zijn geldige sleutels bijvoorbeeld 3, 5, 7, enz., omdat deze getallen copriem zijn met 26. Sleutels als 2, 4 of 6 zijn niet bruikbaar omdat ze gemeenschappelijke factoren hebben met 26, waardoor de versleuteling niet omkeerbaar zou zijn.

```Python
    def ggd(a, b):
    # algoritme van Euclides
        while a != 0:
            a, b = b % a, a
        return b


    if ggd(sleutel, len(SYMBOLS)) == 1:
         # sleutel is valide!

```

## Oefening 9: de vermenigvuldigigingsversleuteling bruteforcen

Jouw opdracht: je gaat een met vermenigvuldigversleuteling geëncrypteerde boodschap decrypteren. Je kent de sleutel niet. Je gaat dus voor elke mogelijke sleutel een decryptie tonen. Je maakt gebruikt van oefening 6 om automatisch de juiste gedecrypteerde boodschap te vinden.


## Oefening 10: "Affiene Versleuteling" of "Affiene Cijfer"

Affiene versleuteling combineert vermenigvuldigigingsversleuteling en Caesar versleuteling. Het woord "affiene" (in het Engels spreken we over Affine cipher) refereert naar het soort wiskundige functies dat gebruikt wordt (affiene transformaties). Een affiene functie is in de wiskunde een functie die een lijn of een deel ervan representeert (elk punt wordt verplaatst langs een constante lijn of vector), en dat is precies wat er gebeurt bij deze versleutelingsmethode: elke letter of symbool wordt langs een zekere "afstand" (vastgesteld door de wiskundige formule) in het alfabet verplaatst om het te coderen. 

Het betreft hier een type substitutiecipher waarbij elke letter in het alfabet wordt gemapt op een andere letter met behulp van een wiskundige functie. Substitutie betekent eenvoudigweg het vervangen van één ding door een ander. Het basisprincipe van de Affiene versleuteling kan worden uitgelegd door de volgende wiskundige uitdrukking:

\[ C \equiv aP + b \mod m \]

Hierin is:
- \( C \) de uitkomst (de gecodeerde letter),
- \( P \) de plaintext letter die je wilt coderen (voorgesteld als een getal waarbij a=0, b=1, ..., z=25),
- \( a \) en \( b \) zijn de sleutels gekozen door degene die de code maakt (en ze moeten bepaalde eigenschappen hebben, zoals dat \( a \) en \( m \) copriem moeten zijn),
- \( m \) is de grootte van het alfabet (in het Engels zou \( m \) 26 zijn: 26 letters),
- "mod" staat voor modulo, een soort rest-na-deling operatie.

Laten we een voorbeeld bekijken om dit concept te verduidelijken:

Stel we kiezen de sleutels \( a = 5 \) en \( b = 8 \), en we willen de letter "h" coderen. Eerst vertalen we de letter "h" naar een getal: h=7 (a=0, b=1, c=2, ..., h=7, ...). Nu vervangen we \( P \) met 7 in onze formule en rekenen we het uit:

\[ C \equiv (5 \times 7 + 8) \mod 26 \]
\[ C \equiv (35 + 8) \mod 26 \]
\[ C \equiv 43 \mod 26 \]
\[ C \equiv 17 \]

Nu vinden we welk karakter overeenkomt met het getal 17: r (a=0, b=1, ..., q=16, r=17, ...). Dus in onze code wordt de letter "h" vervangen door de letter "r".

Om te ontcijferen, moet je de inverse van het getal a vinden (dus een getal dat, wanneer vermenigvuldigd met a, gelijk is aan 1 mod 26). Dit gebruik je dan in de ontcijferformule:

\[ P \equiv a^{-1}(C - b) \mod m \]

- Je bestudeert en zoekt op hoe affiene versleuteling werkt
- Je schrijft een script dat volgens deze versleuteling encrypteert en decrypteert.

## Oefening 11: de affiene versleuteling bruteforcen

Jouw opdracht: je gaat een met vermenigvuldigversleuteling geëncrypteerde boodschap decrypteren. Je kent de sleutel niet. Je gaat dus voor elke mogelijke sleutel een decryptie tonen. Je maakt gebruikt van oefening 6 om automatisch de juiste gedecrypteerde boodschap te vinden.


## Oefening 12: eenvoudige substitutieversleuteling

Eenvoudige substitutieversleuteling is een type cryptografie waarbij elke letter of teken in een tekst wordt vervangen door een andere, volgens een vooraf bepaalde regel of sleutel. Het basisidee is dat elke letter in de originele tekst (de klare tekst) wordt 'vertaald' naar een nieuwe letter, cijfer, of symbool in de versleutelde tekst.

Hier zijn een paar kernpunten:
- **Sleutel**: De methode of regel die gebruikt wordt om letters te vervangen. Dit zou bijvoorbeeld een verschuiving van enkele posities in het alfabet kunnen zijn (zoals bij het Caesar-cijfer) of een meer complexe regel waarbij elke letter in het alfabet een unieke, willekeurige vervanger krijgt.
  
- **Vervanging**: Elke letter in de klare tekst wordt vervangen door de corresponderende letter, cijfer, of symbool volgens de sleutel.

- **Omkeerbaarheid**: Het is cruciaal dat de substitutie omkeerbaar is, zodat de ontvanger de originele tekst kan herstellen door de versleutelde tekst te ontcijferen met de juiste sleutel.

Bijvoorbeeld:
Stel je hebt de volgende sleutel voor substitutieversleuteling:
\[ \text{A B C D E F G H I J K L M N O P Q R S T U V W X Y Z} \]
\[ \text{Q W E R T Y U I O P A S D F G H J K L Z X C V B N M} \]

Dan wordt de letter "A" in de klare tekst vervangen door "Q" in de versleutelde tekst, "B" wordt vervangen door "W", "C" wordt vervangen door "E", enzovoorts. Als we het woord "CODE" willen versleutelen, dan wordt dat "RWTY" volgens de hierboven gegeven sleutel.

De eenvoudige substitutieversleuteling is vrij eenvoudig te begrijpen maar kan, afhankelijk van de sleutel, variëren in complexiteit en veiligheid tegen ontcijfering.

- Je bestudeert en zoekt op hoe eenvoudige substitutieversleuteling werkt
- Je schrijft een script dat volgens deze versleuteling encrypteert en decrypteert.


## Oefening 13: eenvoudige substitutieversleuteling hacken

Schrijf een script dat een met eenvoudige substitutieversleuteling geëncrypteerde boodschap probeert de decrypteren.