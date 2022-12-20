"""
author:leon
project:programmerUpgrade
date:2022/12/12
email:13368447@qq.com
"""
import sys
import pygame

from bullet import Bullet
from alien import Alien


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
    if event.key == pygame.K_ESCAPE:
        sys.exit()
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


def updateScreen(aiSettings, screen, ship, aliens, bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(aiSettings.bgColor)

    # 绘制子弹
    for bullet in bullets.sprites():
        bullet.drawBullet()
    ship.blitme()
    aliens.draw(screen)
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


def getNumberAliensX(aiSettings, alienWidth):
    """计算每行可以容纳多少个外星人"""
    availableSpaceX = aiSettings.screenWidth - 2 * alienWidth
    numberAliensX = int(availableSpaceX / (2 * alienWidth))
    return numberAliensX


def getNumberRows(aiSettings, shipHeight, alienHeight):
    """计算屏幕可容纳多少行外星人"""
    availableSpaceY = (aiSettings.screenHeight - (3 * alienHeight) - shipHeight)
    numberRows = int(availableSpaceY / (2 * alienHeight))
    return numberRows


def createAlien(aiSettings, screen, aliens, alienNumber, rowNumber):
    """创建一个外星人并将其放在当前行"""
    alien = Alien(aiSettings, screen)
    alienWidth = alien.rect.width
    alien.x = alienWidth + 2 * alienWidth * alienNumber
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * rowNumber
    aliens.add(alien)


def createFleet(aiSettings, screen, ship, aliens):
    """创建外星人群"""
    # 外星人间距为外星人宽度
    alien = Alien(aiSettings, screen)
    alienWidth = alien.rect.width
    numberAliensX = getNumberAliensX(aiSettings, alienWidth)
    numberRows = getNumberRows(aiSettings, ship.rect.height, alien.rect.height)
    # 创建外星人群
    for rowNum in range(numberRows):
        for alienNum in range(numberAliensX):
            # 创建一个外星人并将其加入当前行
            createAlien(aiSettings, screen, aliens, alienNum, rowNum)


def checkFleetEdges(aiSettings, aliens):
    """有外星人到达边缘时采取相应的措施"""
    for alien in aliens.sprites():
        if alien.checkEdges():
            changeFleetDirection(aiSettings, aliens)
            break


def changeFleetDirection(aiSettings, aliens):
    """将整群外星人下移，并改变它们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += aiSettings.fleetDropSpeed
    aiSettings.fleetDirection *= -1


def updateAliens(aiSettings, aliens):
    """
    检查是否有外星人位于屏幕边缘，并更新整群外星人的位置
    """
    checkFleetEdges(aiSettings, aliens)
    aliens.update()
