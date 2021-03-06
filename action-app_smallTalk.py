#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from snipsTools import SnipsConfigParser
from xiSnipsTools import Personality
from hermes_python.ontology import *
from hermes_python.hermes import Hermes
from hermes_python.ontology import MqttOptions
from hermes_python.ontology.tts import RegisterSoundMessage

import io
import os
import toml

CONFIG_INI = "config.ini"

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

wdyt_personality = None
hay_personalitiy = None

class SnipsSmallTalk(object):
    """Action Code for the snips App "SmallTalk"
       Smalltalk ist my first test app for snips and in the python prgramming language
    """

    def __init__(self):
        #get the configuration if needed
        try:
           self.config = SnipsConfigParser.read_configuration_file(CONFIG_INI)
        except :
            self.config = None

        # start listening to MQTT
        self.start_blocking()
        
    # --> Sub callback function, one per intent
    def howareyou_callback(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")
        
        # action code goes here...
        print('[Received] intent: {}'.format(intent_message.intent.intent_name))
        
        message = "null"
        # Read CPU temperature
        cpu_temp = os.popen("sh getcputemp.sh").readline()
        
        message = "null"

        try: 
            cpu_temp2 = float(cpu_temp)
        
            if cpu_temp2 < 60:
                message = hay_personality.get_AnswerToTopic("well").format(cpu_temp)
            else:
                message = hay_personality.get_AnswerToTopic("notwell").format(cpu_temp)
        
        except :
            message = hay_personality.get_AnswerToTopic("null")
            print("Fehler bei der Ermittlung der cpu Temperatur \n Mögliche Ursachen:\n 1. Nutzer _snips-skills nicht in Rechtegruppe video\n 2. Skill wird nicht auf Raspberry ausgeführt")

        # if need to speak the execution result by tts
        hermes.publish_start_session_notification(intent_message.site_id, message, "SnipsSmallTalkAPP")

    def whatdoyouthink_callback(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")

        # action code goes here...
        print('[Received] intent: {}'.format(intent_message.intent.intent_name))
        
        message = "null"
        topic = "null"
       
        if len(intent_message.slots.topic) > 0:
            topic = str(intent_message.slots.topic.first().value)
            print("Erkannter Topic Wert: " + topic)
        
        message = wdyt_personality.get_AnswerToTopic(topic)
        print(message)

        # if need to speak the execution result by tts
        hermes.publish_start_session_notification(intent_message.site_id, message, "SnipsSmallTalkAPP")

    def completeidiom_callback(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")

        # action code goes here...
        print('[Received] intent: {}'.format(intent_message.intent.intent_name))
        
        message = "null"
        idiom = str(intent_message.input)
        print("Erkannter Message Idiom Wert: " + idiom)
                
        message = ci_personality.get_AnswerToTopic(idiom)
        print(message)

        # if need to speak the execution result by tts
        hermes.publish_start_session_notification(intent_message.site_id, message, "SnipsSmallTalkAPP")
    
    def tellmeajoke_callback(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")

        # action code goes here...
        print('[Received] intent: {}'.format(intent_message.intent.intent_name))
        
        message = "null"
        category = "null"
        if len(intent_message.slots.category) > 0:
            category = str(intent_message.slots.category.first().value)
            message = tmaj_personality.get_AnswerToTopic(category)
           
        else:
            message = tmaj_personality.get_RandomContent()

        print("Erkannte Witz Kategorie: " + category)
        
        print(message)

        # if need to speak the execution result by tts
        hermes.publish_start_session_notification(intent_message.site_id, message, "SnipsSmallTalkAPP")
        hermes.publish_end_session(intent_message.session_id, "[[sound:test]]")

 

    # --> Master callback function, triggered everytime an intent is recognized
    def master_intent_callback(self,hermes, intent_message):
        coming_intent = intent_message.intent.intent_name
        if coming_intent == 'xion:howareyou':
            self.howareyou_callback(hermes, intent_message)
        if coming_intent == 'xion:whatdoyouthink':
            self.whatdoyouthink_callback(hermes, intent_message)
        if coming_intent == 'xion:completeIdiom':
            self.completeidiom_callback(hermes, intent_message)
        if coming_intent == 'xion:tellmeajoke':
            self.tellmeajoke_callback(hermes, intent_message)

    # --> Register callback function and start MQTT
    def start_blocking(self):
        snips_config = toml.load('/etc/snips.toml')

        mqtt_username = None
        mqtt_password = None
        mqtt_broker_address = "localhost:1883"
        
        if 'mqtt' in snips_config['snips-common'].keys():
            mqtt_broker_address = snips_config['snips-common']['mqtt']
        if 'mqtt_username' in snips_config['snips-common'].keys():
            mqtt_username = snips_config['snips-common']['mqtt_username']
        if 'mqtt_password' in snips_config['snips-common'].keys():
            mqtt_password = snips_config['snips-common']['mqtt_password']

        mqtt_opts = MqttOptions(username=mqtt_username, password=mqtt_password, broker_address=mqtt_broker_address)
        
        #self.hermes = Hermes(mqtt_options=mqtt_opts)
         #with open('sounds/jokes/badumts_extreme.wav', 'rb') as f:
        #    self.hermes.register_sound(RegisterSoundMessage("test", f.read()))

        #todo dieser Aufruf führt zu segmentation fault fehler 139 self.hermes.subscribe_intents(self.master_intent_callback).start()

        with Hermes(mqtt_options=mqtt_opts) as h:
            h.subscribe_intents(self.master_intent_callback).start()

if __name__ == "__main__":
    wdyt_personality = Personality("de_DE","whatdoyouthink")
    hay_personality = Personality("de_DE","howareyou")
    ci_personality = Personality("de_DE","completeidiom")
    tmaj_personality = Personality("de_DE","tellmeajoke")

    SnipsSmallTalk()
