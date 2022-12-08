"""
author:leon
project:programmerUpgrade
date:2022/12/8
email:13368447@qq.com
"""


def countWords(filename):
    try:
        with open(filename) as fileObj:
            contents = fileObj.read()
    except FileNotFoundError:
        print('Sorry, the file {} does not exist.'.format(filename))
    else:
        words = contents.split(' ')
        print('The file {} has about {} words.'.format(filename, len(words)))
