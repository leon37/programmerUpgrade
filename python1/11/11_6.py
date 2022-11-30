'''
author:leon
project:programmerUpgrade
date:2022/11/24
email:13368447@qq.com
'''


# 每次我在 Google 上搜索一个主题时，都不会一次只看一个搜索结果。
# 通过鼠标中键点击搜索结果链接，或在点击时按住CTRL键，我会在一些新的选项卡中打开前几个链接，稍后再来查看。
# 我经常搜索Google，所以这个工作流程（开浏览器，查找一个主题，依次用中键点击几个链接）变得很乏味。
# 如果我只要在命令行中输入查找主题，就能让计算机自动打开浏览器，并在新的选项卡中显示前面几项查询结果，那就太好了。
# 让我们写一个脚本来完成这件事。

import sys
import bs4
import webbrowser
import requests

if len(sys.argv) == 1:
    print('Need a param!')
param = sys.argv[1:]
keyword = ' '.join(param)
print('The keyword is {}'.format(keyword))

res = requests.get('http://google.com/search?q={}'.format(keyword))
print(res.status_code)
try:
    res.raise_for_status()
except Exception as err:
    print('Something wrong happend: {}'.format(str(err)))

print(res.text)
soup = bs4.BeautifulSoup(res.text)
elems = soup.select('.r a')
numOpen = min(5, len(elems))
for i in range(numOpen):
    print(len(elems))
    webbrowser.open('https://google.com' + elems[i].get('href'))

