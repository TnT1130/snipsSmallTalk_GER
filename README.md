[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/snipsco/snips-app-template-py/blob/master/LICENSE)

## Snips-SmallTalk
Dies ist meine Erste Snips App und meine ersten Gehversuche in Python.

Die App haucht Snips, durch verschiedene Easter-Eggs, etwas mehr Persönlichkeit ein und lässt sich ohne Programmieraufwand über Textdateien an die jeweiligen Bedürfnisse anpassen.

## Installation
Einfache Installation über den SnipsStore (im Moment nur deutscher Store).

Danach unter Rasperry Pi den Nutzer _snips-skills in die Gruppe video aufnehmen:
```bash
sudo usermod -aG video _snips-skills 
```
Sollte snips auf einer anderen Plattform installiert sein, muss das Skript getcputemp.sh angepasst werden. Alternativ könnt ihr mir auch etwaige Skripte und Abfragen zur Verfügung stellen und ich integriere sie in dem Code.

## Derzeit implementiert:

###WhatDoYouThink:
Frage Snips nach einem Thema und sie gibt dir eine passende Antwort.
Beispiele: 
- "Was denkst du über Siri?"
- "Was weißt du über Programmierung?"

###HowAreYou: 
Frage Snips wie es ihr geht und sie gibt dir je nach CPU Temperatur eine passende Antwort
Beispiele: 
- "Wie geht es dir?"
- "Was geht ab?"

Hinweis: Funktioniert derzeit nur bei Raspberry Pi und setzt die Aufnahme des Users _snips-skills in die Rechtegruppe "video" voraus.

###CompleteIdiom
Frage Snips nach dem Beginn einer Redewendung und erhalte eine passende Antwort.
Beispiele: 
- "Fischers Fritz"
- "ene mene Miste"
- "sag mal Klettergerüst"


## Struktur der App

```bash
└── snips-app-template-py
    ├── answers                         # Enthält die Textdateien mit Frage<->Antwort Paaren (pro Intent eine textdatei)                       
    ├── action-app_smallTalk.py         # Actioncode für Intends
    ├── xiSnipsTools.py                 # Meine SnipsTools (z.B. Klasse Personality um Topic<->Antwort Paare aus Textdateien zu erhalten)
    ├── snipsTools.py                   # standard SnipsTools --> wird noch nicht verwendet
    ├── getcputemp.sh                   # Skript um CPU Temperatur auszulesen --> Derzeit nur für Raspberry pi
    ├── config.ini.default              # default app configuration --> wird noch nicht verwendet
    ├── requirements.txt                # required dependencies
    └── setup.sh                        # setup script
```

Diese App nutzt als ursprüngliche Grundlage das snips-Template von snipsco, das ich auf python 3 umgestellt habe: (https://github.com/snipsco/snips-actions-templates).

Vielen Dank das ihr mir so einen guten Einstieg in Snips und Python ermöglicht habt.
