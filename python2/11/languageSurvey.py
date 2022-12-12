"""
author:leon
project:programmerUpgrade
date:2022/12/12
email:13368447@qq.com
"""
from survey import AnonymousSurvey

question = 'What language did you first learn to speak?'
mySurvey = AnonymousSurvey(question)

mySurvey.showQuestion()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input('Language: ')
    if response == 'q':
        break
    mySurvey.storeResponse(response)

print("\nThank you to everyone who participated in the survey!")
mySurvey.showResults()