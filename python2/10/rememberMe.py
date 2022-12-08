"""
author:leon
project:programmerUpgrade
date:2022/12/8
email:13368447@qq.com
"""
import json

filename = 'username.json'
try:
    with open(filename) as fileObj:
        username = json.load(fileObj)
except FileNotFoundError:
    username = input('Please enter your name: ')
    with open(filename, 'w') as fileObj:
        json.dump(username, fileObj)
        print('We will remember you when you come back, {}!'.format(username))
else:
    print('Welcome back, {}!'.format(username))
