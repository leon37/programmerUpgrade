"""
author:leon
project:programmerUpgrade
date:2022/12/13
email:13368447@qq.com
"""
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, aiSettings, screen):
        """初始化外星人并设置其起始位置"""
        super(Alien, self).__init__()
        self.screen = screen
        self.aiSettings = aiSettings

        # 加载外星人图像，并设置其rect属性
        self.image = pygame.image.load('image/alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)