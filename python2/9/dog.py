'''
author:leon
project:programmerUpgrade
date:2022/12/6
email:13368447@qq.com
'''


class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + ' is now sitting.')

    def rollOver(self):
        print(self.name.title() + ' rolled over!')

myDog = Dog('Bo', 2)
print(myDog.name, myDog.age)
myDog.sit()
myDog.rollOver()
