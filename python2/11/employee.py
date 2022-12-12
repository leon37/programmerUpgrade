"""
author:leon
project:programmerUpgrade
date:2022/12/12
email:13368447@qq.com
"""

class Employee:
    def __init__(self, firstName, lastName, salary):
        self.firstName =firstName
        self.lastName = lastName
        self.salary = salary

    def giveRaise(self, raises=5000):
        self.salary += raises