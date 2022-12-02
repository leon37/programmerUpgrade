# 就像很难找到一个简单的秒表应用程序一样，也很难找到一个简单的倒计时程序。
# 让我们来写一个倒计时程序，在倒计时结束时报警。

import time, subprocess, os

timeLeft = 3
while timeLeft > 0:
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft -= 1
os.chdir('python1\\automate_online-materials')
subprocess.Popen(['start', 'alarm.wav'], shell=True)