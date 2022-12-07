"""
author:leon
project:programmerUpgrade
date:2022/12/7
email:13368447@qq.com
"""
# 10-3：编写一个程序，提示用户输入其名字；用户作出响应后，将其名字写入到文件guest.txt中。
# name = input('Please enter your name: ')
# with open('guest.txt', 'w') as fileObj:
#     fileObj.write(name)

# 10-4:编写一个while循环，提示用户输入其名字。
# 用户输入其名字后， 在屏幕上打印一句问候语，并将一条访问记录添加到文件guest_book.txt中。
# 确保这个文件中的每条记录都独占一行。
with open('guest_book.txt', 'a') as fileObj:
    while True:
        name = input('Please enter your name: ')
        if name == 'quit':
            break
        fileObj.write(name+'\n')
