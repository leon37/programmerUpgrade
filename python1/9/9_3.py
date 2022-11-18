import zipfile, os

# print(os.getcwd())
os.chdir('.\\python1\\automate_online-materials')
exampleZip = zipfile.ZipFile('example.zip')
print(exampleZip.namelist())

# 获取压缩文件信息
spamInfo = exampleZip.getinfo('spam.txt')
print(spamInfo.file_size)
print(spamInfo.compress_size)

# 解压缩
# exampleZip.extractall()
# exampleZip.extract('spam.txt','./abcdefg')
# exampleZip.close()

# 压缩
newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()
