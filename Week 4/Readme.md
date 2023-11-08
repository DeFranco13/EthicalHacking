# Pentest Framework

## Intro

Dit Framework is opgesteld zodat de gebruiker een website ingeeft met het opstarten van het programma. Vervolgens zullen er verschillende scans worden uitgevoerd op de website.

## Werking

Het commando "python3 main.py <website url>" start het hele process op. De site zal eerst de intro vertonen en vervolgens de data inladen. Er zijn verschillende modules toegepast en de gebruiker kan in de settings.json de modules op true of false zetten als de gebruiker de scans wilt laten uitvoeren. Het script zal eerst deze waardes uitlezen en dan vervolgens de scans die op true staan uitvoeren.

## Strcutuur

Main    ->  Middleman   ->  Intro    
            Middleman   ->  Settings
            Middleman   ->  Brain     ->  Scans   -> Output
