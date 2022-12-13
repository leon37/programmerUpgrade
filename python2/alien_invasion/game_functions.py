"""
author:leon
project:programmerUpgrade
date:2022/12/12
email:13368447@qq.com
"""
import sys
import pygame
from bullet import Bullet


def checkEvents(aiSettings, screen, ship, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            checkKeydownEvents(event, aiSettings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            checkKeyupEvents(event, ship)


def checkKeydownEvents(event, aiSettings, screen, ship, bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.movingRight = True
    if event.key == pygame.K_LEFT:
        ship.movingLeft = True
    if event.key == pygame.K_UP:
        ship.movingUp = True
    if event.key == pygame.K_DOWN:
        ship.movingDown = True
    if event.key == pygame.K_SPACE:
        fireBullet(aiSettings, screen, ship, bullets)


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


def updateScreen(aiSettings, screen, ship, bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(aiSettings.bgColor)

    # 绘制子弹
    for bullet in bullets.sprites():
        bullet.drawBullet()
    ship.blitme()
    # 让最近绘制的屏幕可见
    pygame.display.flip()


def updateBullets(bullets):
    """更新子弹的位置，并删除已经消失的子弹"""
    bullets.update()

    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)


def fireBullet(aiSettings, screen, ship, bullets):
    """如果还没有达到限制，就发射一颗子弹"""
    # 创建新子弹，并将其加入到编组bullets中
    if len(bullets) < aiSettings.bulletAllowed:
        newBullet = Bullet(aiSettings, screen, ship)
        bullets.add(newBullet)
