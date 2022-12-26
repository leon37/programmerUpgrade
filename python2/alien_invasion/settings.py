"""
author:leon
project:programmerUpgrade
date:2022/12/12
email:13368447@qq.com
"""


class Settings():
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screenWidth = 1200
        self.screenHeight = 800
        self.bgColor = (230, 230, 230)

        # 飞船设置
        self.shipSpeedFactor = 1.5
        self.shipLimit = 3

        # 子弹设置
        self.bulletSpeedFactor = 1
        self.bulletWidth = 3
        self.bulletHeight = 15
        self.bulletColor = 60, 60, 60
        self.bulletAllowed = 3

        # 外星人设置
        self.alienSpeedFactor = 0.5
        self.fleetDropSpeed = 5
        # fleetDirection为1表示向右移，为-1表示向左移
        self.fleetDirection = 1
