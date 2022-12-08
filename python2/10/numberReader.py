"""
author:leon
project:programmerUpgrade
date:2022/12/8
email:13368447@qq.com
"""
import json

filename = 'numbers.json'
with open(filename) as fileObj:
    numbers = json.load(fileObj)

print(numbers)
