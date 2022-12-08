"""
author:leon
project:programmerUpgrade
date:2022/12/8
email:13368447@qq.com
"""
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as fileObj:
    json.dump(numbers, fileObj)
