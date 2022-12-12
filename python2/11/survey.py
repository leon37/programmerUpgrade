"""
author:leon
project:programmerUpgrade
date:2022/12/12
email:13368447@qq.com
"""

class AnonymousSurvey():
    def __init__(self, question):
        self.question = question
        self.responses = []

    def showQuestion(self):
        print(self.question)

    def storeResponse(self, newResponse):
        self.responses.append(newResponse)

    def showResults(self):
        print('Survey results:')
        for response in self.responses:
            print('- ' + response)
