"""
author:leon
project:programmerUpgrade
date:2022/12/12
email:13368447@qq.com
"""
import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self) -> None:
        self.employee = Employee('Li', 'Tao', 10000)

    def testGiveDefaultRaise(self):
        origin = self.employee.salary
        self.employee.giveRaise()
        self.assertEqual(origin+5000, self.employee.salary)

    def testGiveCustomRaise(self):
        origin = self.employee.salary
        customRaise = 7500
        self.employee.giveRaise(customRaise)
        self.assertEqual(origin+customRaise, self.employee.salary)

unittest.main()
