'''
author:leon
project:programmerUpgrade
date:2022/11/30
email:13368447@qq.com
'''
import PyPDF2
import os

# 读pdf

# pdfFileObj = open('../automate_online-materials/meetingminutes.pdf', 'rb')
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# print(pdfReader.numPages)
#
# pageObj = pdfReader.getPage(0)
# print(pageObj.extractText())

# pdfReader = PyPDF2.PdfFileReader(open('../automate_online-materials/encrypted.pdf', 'rb'))
# print(pdfReader.isEncrypted)
# # print(pdfReader.getPage(0))
# pdfReader.decrypt('rosebud')
# print(pdfReader.getPage(0).extractText())
os.chdir('../automate_online-materials')

# 写pdf

# pdf1File = open('meetingminutes.pdf', 'rb')
# pdf2File = open('meetingminutes2.pdf', 'rb')
# pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
# pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
#
# pdfWriter = PyPDF2.PdfFileWriter()
# for pageNum in range(pdf1Reader.numPages):
#     pageObj = pdf1Reader.getPage(pageNum)
#     pdfWriter.addPage(pageObj)
#
# for pageNum in range(pdf2Reader.numPages):
#     pageObj = pdf2Reader.getPage(pageNum)
#     pdfWriter.addPage(pageObj)
#
# pdfOutputFile = open('combinedminutes.pdf', 'wb')
# pdfWriter.write(pdfOutputFile)
# pdfOutputFile.close()
# pdf1File.close()
# pdf2File.close()

# 旋转pdf

# minutesFile = open('meetingminutes.pdf', 'rb')
# pdfReader = PyPDF2.PdfFileReader(minutesFile)
# page = pdfReader.getPage(0)
# page.rotateClockwise(90)
#
# pdfWriter = PyPDF2.PdfFileWriter()
# pdfWriter.addPage(page)
# resultFile = open('rotateFile.pdf', 'wb')
# pdfWriter.write(resultFile)
# resultFile.close()
# minutesFile.close()

# 叠加pdf

# minutesFile = open('meetingminutes.pdf', 'rb')
# pdfReader = PyPDF2.PdfFileReader(minutesFile)
# minutesFirstPage = pdfReader.getPage(0)
#
# pdfWatermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf','rb'))
# minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))
#
# pdfWriter = PyPDF2.PdfFileWriter()
# pdfWriter.addPage(minutesFirstPage)
# for pageNum in range(1, pdfReader.numPages):
#     pageObj = pdfReader.getPage(pageNum)
#     pdfWriter.addPage(pageObj)
# resultFile = open('watermarkedCover.pdf', 'wb')
# pdfWriter.write(resultFile)
# minutesFile.close()
# resultFile.close()

# 加密pdf

pdfFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWriter = PyPDF2.PdfFileWriter()
for i in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(i))

pdfWriter.encrypt('swordfish')
resultFile = open('encryptedminutes.pdf', 'wb')
pdfWriter.write(resultFile)
resultFile.close()
pdfFile.close()