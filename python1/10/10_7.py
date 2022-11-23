'''
author:leon
project:programmerUpgrade
date:2022/11/22
email:13368447@qq.com
'''
# 1. 写一条assert语句，如果变量spam是一个小于10的数，就触发AssertionError。
spam = input()
assert int(spam) >= 10, 'The input num should greater than 10.'

# 2. 编写一条assert语句，如果eggs和bacon包含的字符串彼此相同，且不论大小写如何，就触发AssertionError。
eggs = ''
bacon = ''
assert eggs.lower() == bacon.lower(), 'The eggs and bacon can\'t be the same.'

# 3.总能触发的assert
assert False, 'Always assert.'
