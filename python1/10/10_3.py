# 断言
# podBayDoorStatus = 'dd'
# assert podBayDoorStatus == 'open', 'The pod bay must be open.'

# 假定你在编写一个交通信号灯的模拟程序。
# 代表路口信号灯的数据结构是一个字典，以 'ns' 和'ew' 为键，分别表示南北向和东西向的信号灯。
# 这些键的值可以是 'green'、'yellow' 或 'red' 之一。
market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}

def switchLights(stoplight:dict):
    # 确保始终有红灯
    assert 'red' in stoplight.values(), 'Neither light is red: ' + str(stoplight)
    for v in stoplight.values():
        if v == 'green':
            v = 'yellow'
        elif v == 'yellow':
            v = 'red'
        elif v == 'red':
            v = 'green'

switchLights(market_2nd)


