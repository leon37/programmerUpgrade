"""
author:leon
project:programmerUpgrade
date:2022/12/12
email:13368447@qq.com
"""
import pygame


class Ship():
    def __init__(self, aiSettings, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.aiSettings = aiSettings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()
        self.screenRect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screenRect.centerx
        self.rect.bottom = self.screenRect.bottom

        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        print('x:{}, y:{}'.format(self.centerx, self.centery))
        print('screen.top:{}, screen.bottom:{}'.format(self.screenRect.top, self.screenRect.bottom))
        # 移动标志
        self.movingRight = False
        self.movingLeft = False
        self.movingUp = False
        self.movingDown = False

    def update(self):
        if self.movingRight and self.rect.right < self.screenRect.right:
            self.centerx += self.aiSettings.shipSpeedFactor
        if self.movingLeft and self.rect.left > 0:
            self.centerx -= self.aiSettings.shipSpeedFactor
        if self.movingUp and self.rect.top > self.screenRect.top:
            self.centery -= self.aiSettings.shipSpeedFactor
        if self.movingDown and self.rect.bottom < self.screenRect.bottom:
            self.centery += self.aiSettings.shipSpeedFactor

        # 更新rect对象
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
