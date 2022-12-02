'''
author:leon
project:programmerUpgrade
date:2022/12/2
email:13368447@qq.com
'''
import threading
import time

print('Start of program.')


def takeANap():
    time.sleep(5)
    print('Wake up!')


threadObj = threading.Thread(target=takeANap)
threadObj.start()

print('End of program.')

# 向线程的目标函数传递参数

# threadObj = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'], kwargs={'sep': ' & '})
# 错误写法 ==> threadObj = threading.Thread(target=print(['Cats', 'Dogs', 'Frogs'], sep=' & '))
# threadObj.start()