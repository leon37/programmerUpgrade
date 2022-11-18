import shutil
import os

# 复制文件和文件夹
os.chdir('E:\\')
# os.mkdir('delicious')
# f = open('spam.txt', 'w')
# f.write('Hello')
# f.close()
# print(shutil.copy('spam.txt', 'delicious'))

# os.makedirs('a\\b\\c')
# shutil.copytree('a','d')

# 文件和文件夹的移动和改名
# print(shutil.move('工具\\spam1.txt', 'spam.txt'))

# 永久删除文件和文件夹
# os.unlink('111\\341.txt')
# os.rmdir('111') dir里有东西删不掉
# shutil.rmtree('111')  递归删除

# 用send2trash模块安全删除
# send2trash.send2trash(fileName) 发送文件到回收站