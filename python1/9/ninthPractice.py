# 编写一个程序，遍历一个目录树，查找特定扩展名的文件（诸如.pdf或.jpg）。
# 不论这些文件的位置在哪里，将它们拷贝到一个新的文件夹中。
import os
import shutil

def copySpecifiedFile(root, suffix, dest):
    for folder, subfolder, fileName in os.walk(root):
        if fileName.endswith(suffix):
            shutil.copy(os.path.join(folder, fileName), dest)
