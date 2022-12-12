"""
author:leon
project:programmerUpgrade
date:2022/12/12
email:13368447@qq.com
"""
import unittest
from nameFunction import getFormattedName

class NamesTestCase(unittest.TestCase):

    def testFirstLastName(self):
        formattedName = getFormattedName('janis', 'joplin')
        self.assertEqual(formattedName, 'Janis Joplin')

    def testFirstLastMiddleName(self):
        formattedName = getFormattedName('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formattedName, 'Wolfgang Amadeus Mozart')

unittest.main()
