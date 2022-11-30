# 这个项目需要编写一个程序，更新产品销售电子表格中的单元格。
# 程序将遍历这个电子表格，找到特定类型的产品，并更新它们的价格。
# 每一行代表一次单独的销售。列分别是销售产品的类型（A）、产品每磅的价格（B）、销售的磅数（C），以及这次销售的总收入。
# TOTAL列设置为Excel公式，将每磅的成本乘以销售的磅数，并将结果取整到分。
# 有了这个公式，如果列B或C发生变化，TOTAL列中的单元格将自动更新。
# 现在假设Garlic、Celery和Lemons的价格输入的不正确。
# 这让你面对一项无聊的任务：遍历这个电子表格中的几千行，更新所有garlic、celery和lemon行中每磅的价格。
# 你不能简单地对价格查找替换，因为可能有其他的产品价格一样，你不希望错误地“更正”。
# 对于几千行数据，手工操作可能要几小时。但你可以编写程序，几秒钟内完成这个任务。

# 需要更新的价格如下：
# Celery 　　 1.19
# Garlic 　　 3.07
# Lemon 　　 1.27
#! python3
import os, openpyxl

os.chdir('python1')
wb = openpyxl.load_workbook('automate_online-materials\\produceSales.xlsx')
sheet = wb.get_sheet_by_name('Sheet')
priceUpdate = {
    'Garlic': 3.07,
    'Celery': 1.19,
    'Lemon': 1.27
}
print(sheet.max_row, sheet.max_column)
for rowNum in range(2, sheet.max_row+1):
    produceName=sheet.cell(row=rowNum, column=1).value
    if produceName in priceUpdate:
        count=sheet.cell(row=rowNum, column=3).value
        sheet.cell(row=rowNum, column=2).value=priceUpdate[produceName]
        sheet.cell(row=rowNum, column=4).value=priceUpdate[produceName]*count

wb.save('updatedProduceSales.xlsx')