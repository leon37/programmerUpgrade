"""
author:leon
project:programmerUpgrade
date:2022/12/12
email:13368447@qq.com
"""
import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def runGame():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    aiSettings = Settings()
    screen = pygame.display.set_mode((aiSettings.screenWidth, aiSettings.screenHeight))
    pygame.display.set_caption('Alien Invasion')

    # 创建一艘飞船
    ship = Ship(aiSettings, screen)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标
        gf.checkEvents(ship)
        ship.update()
        gf.updateScreen(aiSettings, screen, ship)


runGame()
