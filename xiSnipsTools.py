import random

class Personality:
    def __init__(self, language):
        self.language = language
        self.answerDict = {}
        self.load_Answers()

    def load_Answers(self):
        #with open(lang + '/' + slotname + '/dict.txt') as fileobj:
        with open('answers.txt') as fileobj:
            for line in fileobj:
               key, value = line.split(":")
               self.answerDict[key] = value
    
    def get_AnswerToTopic(self, topic):

        try:
            answerList = self.answerDict[topic].split(";")
        
        except:
            return str(random.choice(self.answerDict["null"].split(";")))
        
        return str(random.choice(answerList))
        