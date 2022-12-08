"""
author:leon
project:programmerUpgrade
date:2022/12/9
email:13368447@qq.com
"""
from nameFunction import getFormattedName

print("Enter 'q' at any time to quit.")
while True:
    first = input('\nPlease give me a first name: ')
    if first == 'q':
        break
    last = input('Please give me a last name: ')
    if last == 'q':
        break
    formattedName = getFormattedName(first, last)
    print('\tNearly formatted name: ' + formattedName + '.')
