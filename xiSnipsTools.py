import random
from hermes_python.hermes import Hermes
from hermes_python.ontology.tts import RegisterSoundMessage

#from hermes_python.ontology.injection import InjectionRequestMessage, AddFromVanillaInjectionRequest

class Personality:
    def __init__(self, language, intent):
        self.language = language
        self.answerDict = {}
        self.load_Answers(intent)
        self.registerSounds()

    def load_Answers(self, intent):
        #with open(lang + '/' + slotname + '/dict.txt') as fileobj:
        with open('answers/'+str(intent)+'_answers.txt') as fileobj:
            for line in fileobj:
               key, value = line.split(":")
               self.answerDict[key] = value
    
    def get_AnswerToTopic(self, topic):

        try:
            answerList = self.answerDict[topic].split(";")
        
        except:
            print("Problem: konnte gesuchte Antwort zu Topic nicht finden. Topic: "+topic)
            return str(random.choice(self.answerDict["null"].split(";")))
            
        return str(random.choice(answerList))
    
    def get_RandomContent(self):
        # muss getestet werden
        return str(random.choice(random.choice(list(self.answerDict.values())).split(";")))
    

    def registerSounds(self):
        #todo: sound Ordner rekursiv nach dateinamen mit .wav durchsuchen und alle registrieren. Wenn kein Ordner oder Dateien, dann abbrechen
        with open('sounds/jokes/badumts_extreme.wav', 'rb') as f:
            self.hermes.register_sound(RegisterSoundMessage("test", f.read()))

    #Todo How can i read the default training data and then inject only the untrained entities?
    """def inject_Entities(self, entities):
         self.hermes.request_injection(InjectionRequestMessage([
            AddFromVanillaInjectionRequest(entities)
        ]))
    """