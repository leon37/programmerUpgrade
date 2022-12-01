'''
author:leon
project:programmerUpgrade
date:2022/11/30
email:13368447@qq.com
'''
# 假定你有一个很无聊的任务，需要将几十个PDF文件合并成一个PDF文件。
# 每一个文件都有一个封面作为第一页，但你不希望合并后的文件中重复出现这些封面。
# 即使有许多免费的程序可以合并PDF，很多也只是简单的将文件合并在一起。
# 让我们来写一个Python程序，定制需要合并到PDF中的页面。

import PyPDF2, os

pdfFiles = []
os.chdir('python1\\automate_online-materials')
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort()
print(pdfFiles)
pdfWriter = PyPDF2.PdfFileWriter()

for pdfFilename in pdfFiles:
    # print(os.path.join(os.path.abspath('.'),pdfFilename))
    pdfFile = open(os.path.join(os.path.abspath('.'),pdfFilename), 'rb')
    pdfFileReader = PyPDF2.PdfFileReader(pdfFile)
    pdfFileReader.rea
    for pageNum in range(1, pdfFileReader.numPages):
        pdfWriter.addPage(pdfFileReader.getPage(pageNum))
    pdfFile.close()

resultFile = open('allminutes.pdf', 'wb')
pdfWriter.write(resultFile)
resultFile.close()