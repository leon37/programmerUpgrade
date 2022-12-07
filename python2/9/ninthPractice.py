'''
author:leon
project:programmerUpgrade
date:2022/12/6
email:13368447@qq.com
'''


# 9-1 9-4

class Restaurant:
    def __init__(self, restaurantName, cuisineType):
        self.name = restaurantName
        self.type = cuisineType
        self.numberServed = 0

    def describeRestaurant(self):
        print('The restaurant name is {}, its cuisine type is {}'.format(self.name, self.type))

    def openRestaurant(self):
        print('The restaurant is opening.')

    def setNumberServed(self, num):
        self.numberServed = num

    def incrementNumberServed(self, num):
        self.numberServed += num


r = Restaurant('baozidian', 'eee')
r.describeRestaurant()
r.openRestaurant()


# 9-6

class IceCreamStand(Restaurant):
    def __init__(self, restaurantName, cuisineType):
        super().__init__(restaurantName, cuisineType)
        self.flavors = []

    def getFlavors(self):
        print(self.flavors)
