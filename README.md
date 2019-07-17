[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/snipsco/snips-app-template-py/blob/master/LICENSE)

## Snips-SmallTalk


## Installation



## Struktur der App

```bash
└── snips-app-template-py                                
    ├── action-app_smallTalk.py         # Actioncode für Intends
    ├── xiSnipsTools.py                 # Meine SnipsTools (z.B. Klasse Personality um Topic<->Antwort Paare aus Textdateien zu erhalten)
    ├── snipsTools.py                   # standard SnipsTools --> wird noch nicht verwendet
    ├── getcputemp.sh                   # Skript um CPU Temperatur auszulesen --> Derzeit nur für Raspberry pi
    ├── <intentname1>_answers.txt       # Textdateien für Topic<->Antort Paare je nach Intent (z.B. whatdoyouthink_answers.txt)
    ├── config.ini.default              # default app configuration --> wird noch nicht verwendet
    ├── requirements.txt                # required dependencies
    └── setup.sh                        # setup script
```

Diese App nutzt als ursprüngliche Grundlage das snips-Template von snipsco, das ich auf python 3 umgestellt habe: (https://github.com/snipsco/snips-actions-templates)
Vielen Dank das ihr mir so einen guten Einstieg in Snips und Python ermöglicht habt.
