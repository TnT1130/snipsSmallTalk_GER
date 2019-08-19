import random

class Personality:
    def __init__(self, language, intent):
        self.language = language
        self.answerDict = {}
        self.load_Answers(intent)
        self.getSoundNames()

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
    

    def getSoundNames(self):
        #todo: sound Ordner rekursiv nach dateinamen mit .wav durchsuchen und alle registrieren. Wenn kein Ordner oder Dateien, dann abbrechen
        return