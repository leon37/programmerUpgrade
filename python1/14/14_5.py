# 检查天气似乎相当简单：打开Web浏览器，点击地址栏，输入天气网站的
# URL（或搜索一个，然后点击链接），等待页面加载，跳过所有的广告等。
# 其实，如果有一个程序，下载今后几天的天气预报，并以纯文本打印出来，
# 就可以跳过很多无聊的步骤。该程序利用第11章介绍的requests模块，
# 从网站下载数据。
import requests
import json
import sys

if len(sys.argv) < 2:
    print('Usage: 14_5.py location')
    sys.exit()

location = ' '.join(sys.argv[1:])
url ='http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % (location)
response = requests.get(url)
response.raise_for_status()

weatherData = json.loads(response.text)
