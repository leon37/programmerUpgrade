"""
author:leon
project:programmerUpgrade
date:2022/12/13
email:13368447@qq.com
"""
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, aiSettings, screen, ship):
        """在飞船所处的位置创建一个子弹对象"""
        super(Bullet, self).__init__()
        self.screen = screen

        # 在(0,0)处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, aiSettings.bulletWidth, aiSettings.bulletHeight)
        self.rect.centerx = ship.rect.centerx
        self.rect.centery = ship.rect.top

        # 存储用小数表示的子弹位置
        self.y = float(self.rect.y)

        self.color = aiSettings.bulletColor
        self.speedFactor = aiSettings.bulletSpeedFactor

    def update(self):
        """向上移动子弹"""
        self.y -= self.speedFactor
        self.rect.y = self.y

    def drawBullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)


