"""
author:leon
project:programmerUpgrade
date:2022/12/7
email:13368447@qq.com
"""


class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometerReading = 0

    def getDescriptiveName(self):
        longName = ' '.join([str(self.year), self.make, self.model])
        return longName.title()

    def readOdometer(self):
        print('This car has ' + str(self.odometerReading) + ' miles on it.')

    def updateOdometer(self, mileage):
        if mileage >= self.odometerReading:
            self.odometerReading = mileage
        else:
            print('You can\'t roll back on odometer!')

    def incrementOdometer(self, miles):
        self.odometerReading += miles

    def fillGasTank(self):
        print('This car\'s gas tank has been filled.')


myNewCar = Car('chevrolet', 'malibu', '2021')
print(myNewCar.getDescriptiveName())
myNewCar.updateOdometer(15021)
myNewCar.readOdometer()