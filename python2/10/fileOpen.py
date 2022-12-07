"""
author:leon
project:programmerUpgrade
date:2022/12/7
email:13368447@qq.com
"""

fileName = 'pi_million_digits.txt'

with open(fileName, 'r') as fileObject:  # 关键字 with 在不再访问文件后关闭 相当于go中的 defer file.Close()
    # contents = fileObject.read()
    # print(contents)
    lines = fileObject.readlines()


piString = ''
for line in lines:
    piString += line.strip()

birthDay = input('Enter your birthday, in the form mmddyy: ')
if birthDay in piString:
    print('Your birthday appears in the first million digits of pi!')
else:
    print("Your birthday does not appear in the first million digits of pi.")
