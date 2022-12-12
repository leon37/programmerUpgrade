"""
author:leon
project:programmerUpgrade
date:2022/12/12
email:13368447@qq.com
"""
import sys
import pygame


def checkEvents(ship):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            checkKeydownEvents(event, ship)

        elif event.type == pygame.KEYUP:
            checkKeyupEvents(event, ship)


def checkKeydownEvents(event, ship):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.movingRight = True
    if event.key == pygame.K_LEFT:
        ship.movingLeft = True
    if event.key == pygame.K_UP:
        ship.movingUp = True
    if event.key == pygame.K_DOWN:
        ship.movingDown = True


def checkKeyupEvents(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.movingRight = False
    if event.key == pygame.K_LEFT:
        ship.movingLeft = False
    if event.key == pygame.K_UP:
        ship.movingUp = False
    if event.key == pygame.K_DOWN:
        ship.movingDown = False


def updateScreen(aiSettings, screen, ship):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(aiSettings.bgColor)
    ship.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()
