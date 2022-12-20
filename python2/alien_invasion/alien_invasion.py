"""
author:leon
project:programmerUpgrade
date:2022/12/12
email:13368447@qq.com
"""
import sys
import pygame
import game_functions as gf

from settings import Settings
from ship import Ship
from pygame.sprite import Group


def runGame():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    aiSettings = Settings()
    screen = pygame.display.set_mode((aiSettings.screenWidth, aiSettings.screenHeight))
    pygame.display.set_caption('Alien Invasion')

    # 创建一艘飞船
    ship = Ship(aiSettings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建一个外星人编组
    aliens = Group()

    # 创建外星人群
    gf.createFleet(aiSettings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标
        gf.checkEvents(aiSettings, screen, ship, bullets)
        ship.update()
        gf.updateBullets(bullets)
        gf.updateAliens(aiSettings, aliens)
        gf.updateScreen(aiSettings, screen, ship, aliens, bullets)


runGame()
