import pprint
import openpyxl
import os

os.chdir('python1')
wb = openpyxl.load_workbook('automate_online-materials\\censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')
# print(sheet.title)
countryData = {}

for row in range(2, sheet.max_row+1):
    state = sheet['B' + str(row)].value
    country = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    countryData.setdefault(state, {})
    countryData[state].setdefault(country, {'tracts':0, 'pop': 0})

    countryData[state][country]['tracts'] += 1
    countryData[state][country]['pop'] += int(pop)

print('Writing results...')
resultFile = open('census2010.py','w')
resultFile.write('allData = ' + pprint.pformat(countryData))
resultFile.close()