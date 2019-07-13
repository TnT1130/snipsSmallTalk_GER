# Entwurf
class Personality:
    def __init__(self, language):
        self.language = language
        self.answerDict = {}

    def load_Anwwers(self):
        #with open(lang + '/' + slotname + '/dict.txt') as fileobj:
        with open('dict.txt') as fileobj:
            for line in fileobj:
               key, value = line.split(":")
               self.answerDict[key] = value
    
    def get_AnswerToTopic(self, topic):
        return self.answerDict[topic]



