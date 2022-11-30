# 设置某些单元格行或列的字体风格，可以帮助你强调电子表格中重点的区域。
# 例如，在这个产品电子表格中，程序可以对potato、garlic和parsnip等行使用粗体。
# 或者也许你希望对每磅价格超过5美元的行使用斜体。
# 手工为大型电子表格的某些部分设置字体风格非常令人厌烦，但程序可以马上完成。
import openpyxl
from openpyxl.styles import Font, NamedStyle

wb = openpyxl.Workbook()
sheet = wb.get_sheet_by_name('Sheet')
italic24Font = Font(size=24, italic=True)
styleObj = NamedStyle(font=italic24Font,name='test')

sheet['A1'].style=styleObj
sheet['A1'] = 'Hello world'
wb.save('styled.xlsx')