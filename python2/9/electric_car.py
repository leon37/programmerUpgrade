"""
author:leon
project:programmerUpgrade
date:2022/12/7
email:13368447@qq.com
"""
from car import Car
from battery import Battery


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery(80)

    # def describeBattery(self):
    #     print('This car has a ' + str(self.batterySize) + '-kWh battery.')

    def fillGasTank(self):
        print('This car doesn\'t need a gas tank!')


myTesla = ElectricCar('tesla', 'model s', 2016)
print(myTesla.getDescriptiveName())
# myTesla.describeBattery()
myTesla.fillGasTank()
myTesla.battery.describeBattery()
myTesla.battery.getRange()