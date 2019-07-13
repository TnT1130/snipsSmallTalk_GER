#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from snipsTools import SnipsConfigParser
from hermes_python.hermes import Hermes
from hermes_python.ontology import *
import io
import os

CONFIG_INI = "config.ini"

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

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
        
        try: 
            cpu_temp2 = float(cpu_temp)
        
            if cpu_temp2 < 60:
                message = 'Ganz gut! Mein Körper ist {} grad warm.'.format(cpu_temp)
            else:
                message = 'Nicht so gut! Mein Körper ist {} Grad heiß. Kannst du da was machen?'.format(cpu_temp)
        
        except :
            message = "Ich weiß nicht so genau. Ich konnte meine Temperatur nicht ermitteln."
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
            topic = intent_message.slots.topic.first().value
        
        if topic == "Trump":
            message = "Ich verstehe leider nicht viel von der Welt. Er wohl auch nicht."

        if topic == "null":
            message = "Ein Bewusstsein wurde leider noch nicht implementiert. Selbständiges denken klappt also nicht."

        # if need to speak the execution result by tts
        hermes.publish_start_session_notification(intent_message.site_id, message, "SnipsSmallTalkAPP")

    # More callback function goes here...

    # --> Master callback function, triggered everytime an intent is recognized
    def master_intent_callback(self,hermes, intent_message):
        coming_intent = intent_message.intent.intent_name
        if coming_intent == 'xion:howareyou':
            self.howareyou_callback(hermes, intent_message)
        if coming_intent == 'xion:whatdoyouthink':
            self.whatdoyouthink_callback(hermes, intent_message)

        # more callback and if condition goes here...

    # --> Register callback function and start MQTT
    def start_blocking(self):
        with Hermes(MQTT_ADDR) as h:
            h.subscribe_intents(self.master_intent_callback).start()

if __name__ == "__main__":
    SnipsSmallTalk()
