"""
author:leon
project:programmerUpgrade
date:2022/12/7
email:13368447@qq.com
"""


class Battery:
    def __init__(self, batterySize=70):
        self.batterySize = batterySize

    def describeBattery(self):
        print('This car has a ' + str(self.batterySize) + '-kWh battery.')

    def getRange(self):
        range = 0
        if self.batterySize == 70:
            range = 240
        elif self.batterySize == 85:
            range = 270

    def upgradeBattery(self):
        if self.batterySize != 85:
            self.batterySize = 85

        message = 'This car can go approximately ' + str(range)
        message += ' miles on a full charge.'
        print(message)
