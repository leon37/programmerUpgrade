"""
author:leon
project:programmerUpgrade
date:2022/12/9
email:13368447@qq.com
"""


def getFormattedName(first, last, middle=''):
    if middle:
        fullName = first + ' ' + middle + ' ' + last
    else:
        fullName = first + ' ' + last
    return fullName.title()
