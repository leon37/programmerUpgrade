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
        self.shipSpeedFactor = 1.5

        # 子弹设置
        self.bulletSpeedFactor = 1
        self.bulletWidth = 3
        self.bulletHeight = 15
        self.bulletColor = 60, 60, 60
        self.bulletAllowed = 3