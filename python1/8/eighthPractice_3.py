# 编写一个程序，打开文件夹中所有的.txt文件，查找匹配用户提供的正则表达式的所有行。
# 结果应该打印到屏幕上。

import os
import re

reg = re.compile('\d{3}-\d{4}-\d{4}')

for fileName in os.listdir('.'):
    if fileName.endswith('.txt'):
        file = open(fileName)
        contents = file.readlines()
        for content in contents:
            mo = reg.search(content)
            if mo:
                print('fileName: %s, lineContent: %s'% (fileName, content))
