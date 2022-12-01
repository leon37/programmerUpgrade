'''
author:leon
project:programmerUpgrade
date:2022/12/1
email:13368447@qq.com
'''
import datetime
import time

# print(datetime.datetime.now())
# dt = datetime.datetime(2015, 10, 21, 16, 29, 0)
# print(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)

# print(datetime.datetime.fromtimestamp(time.time()))

# timedelta数据类型
# delta = datetime.timedelta(days=9, hours=10, minutes=11, seconds=12)
# print(delta.days, delta.seconds, delta.microseconds)

# print(delta.total_seconds())
# print(str(delta))

# dt = datetime.datetime(2019, 2, 7)
# delta = datetime.timedelta(days=1111)
# print(dt+delta)

# 暂停直至特定日期
# halloween2016 = datetime.datetime(2023, 1, 1, 0, 0, 0)
# while datetime.datetime.now() < halloween2016:
#     time.sleep(30)

# 将datetime对象转换为字符串
# today = datetime.datetime(2022,12,2,12,14,0)
# print(today.strftime('%Y--%m--%d %H:%M:%S'))

# 将字符串转换为datetime对象
print(datetime.datetime.strptime('October 21, 2015', '%B %d, %Y'))