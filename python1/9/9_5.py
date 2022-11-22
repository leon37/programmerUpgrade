# 假定你正在做一个项目，它的文件保存在C:\AlsPythonBook文件夹中。
# 你担心工作会丢失，所以希望为整个文件夹创建一个ZIP文件，作为“快照”。
# 你希望保存不同的版本，希望ZIP文件的文件名每次创建时都有所变化。
# 例如AlsPythonBook_1.zip、AlsPythonBook_2.zip、AlsPythonBook_3.zip，等等。

import zipfile
import os

def backupToZip(folder):
    folder = os.path.abspath(folder)

    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break

        number += 1
        file = zipfile.ZipFile(folder, 'w')
        for folderName, subfolders, filenames in os.walk(folder):
            file.write(folderName)
            for fileName in filenames:
                newBase = os.path.basename(folder) + '_'
                if fileName.startswith(newBase) and fileName.endswith('.zip'):
                    continue
                file.write(os.path.join(folderName, fileName))
        file.close()
