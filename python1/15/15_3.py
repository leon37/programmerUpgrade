'''
author:leon
project:programmerUpgrade
date:2022/12/1
email:13368447@qq.com
'''
# 假设要记录在没有自动化的枯燥任务上花了多少时间。
# 你没有物理秒表，要为笔记本或智能手机找到一个免费的秒表应用，
# 没有广告，且不会将你的浏览历史发送给市场营销人员，
# 又出乎意料地困难。你可以自己用python写一个简单的秒表程序。

import time

print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input()
print('Started.')
startTime = time.time()
lastTime = startTime
lapNum = 1

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time()
except KeyboardInterrupt:
    print('\nDone.')