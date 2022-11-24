'''
author:leon
project:programmerUpgrade
date:2022/11/24
email:13368447@qq.com
'''
import bs4

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile)
print(type(exampleSoup))

elems = exampleSoup.select('#author')
print(type(elems))
print(len(elems))
print(type(elems[0]))
print(elems[0].getText())
print(str(elems[0]))
print(elems[0].attrs)

spanElem = exampleSoup.select('span')[0]
print(spanElem.get('id'))

