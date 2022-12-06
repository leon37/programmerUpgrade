'''
author:leon
project:programmerUpgrade
date:2022/12/6
email:13368447@qq.com
'''

# 9-1

class Restaurant:
    def __init__(self, restaurantName, cuisineType):
        self.name = restaurantName
        self.type = cuisineType

    def describeRestaurant(self):
        print('The restaurant name is {}, its cuisine type is {}'.format(self.name, self.type))

    def openRestaurant(self):
        print('The restaurant is opening.')

r = Restaurant('baozidian', 'eee')
r.describeRestaurant()
r.openRestaurant()