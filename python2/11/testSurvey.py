"""
author:leon
project:programmerUpgrade
date:2022/12/12
email:13368447@qq.com
"""
import unittest
from survey import AnonymousSurvey


class TestAnonymounsSurvey(unittest.TestCase):

    def setUp(self) -> None:
        question = "What language did you first learn to speak?"
        self.mySurvey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def testStoreSingleResponse(self):
        self.mySurvey.storeResponse('English')
        self.assertIn('English', self.mySurvey.responses)

    def testStoreThreeResponses(self):
        for response in self.responses:
            self.mySurvey.storeResponse(response)

        for response in self.responses:
            self.assertIn(response, self.mySurvey.responses)


unittest.main()
