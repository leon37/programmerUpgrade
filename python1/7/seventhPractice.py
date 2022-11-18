import re

# 7.18.1
# 写一个函数，它使用正则表达式，确保传入的口令字符串是强口令。
# 强口令的定义是：长度不少于8个字符，同时包含大写和小写字符，至少有一位数字。
# 你可能需要用多个正则表达式来测试该字符串，以保证它的强度


def check(s):
    # first check length
    lengthRegex = re.compile(r'.{8,}')
    mo = lengthRegex.search(s)
    if not mo:
        print('length invalid.')
        return

    # 检查是否包含大小写字母
    alphaRegex1 = re.compile(r'[a-z]+')
    alphaRegex2 = re.compile(r'[A-Z]+')
    mo1 = alphaRegex1.search(s)
    mo2 = alphaRegex2.search(s)
    if not mo1 or not mo2:
        print('alpha')
        return

    # 检查是否至少有一位数字
    numRegex = re.compile(r'\d+')
    mo = numRegex.search(s)
    if not mo:
        print('one number has to be involved at least.')
        return
    print('check done.')


# check('sssssS3s')

# 7.18.2
# 写一个函数，它接受一个字符串，做的事情和strip()字符串方法一样。
# 如果只传入了要去除的字符串，没有其他参数，那么就从该字符串首尾去除空白字符。
# 否则，函数第二个参数指定的字符将从该字符串中去除
def anotherStrip(s, param=None):
    if not param:
        spaceRegex = re.compile(r'^\s+|\s+$')
        mo = spaceRegex.search(s)
        g = mo.group()
        ss = spaceRegex.sub('',s)
        print(ss)
        print(len(ss))
        return
    else:
        paramRegex = re.compile(r'{}'.format(param))
        ss = paramRegex.sub('', s)
        print(ss)
        print(len(ss))
        return

# s = 'ssddddajkhddddss'
# anotherStrip(s,'ssd')
