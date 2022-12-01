import csv
import os

os.chdir('python1\\automate_online-materials')

# Reader对象
# exampleFile = open('example.csv')
# exampleReader = csv.reader(exampleFile)
# exampleData = list(exampleReader)

# print(exampleData)    

# 在for循环中，从Reader对象读取数据
# exampleFile = open('example.csv')
# exampleReader = csv.reader(exampleFile)
# for row in exampleReader:
#     print('Row #' + str(exampleReader.line_num) + ' ' + str(row))

# Writer对象
# outputFile = open('output.csv', 'w', newline='')
# outputWriter = csv.writer(outputFile)
# outputWriter.writerow(['spam','eggs','bacon','ham'])
# outputFile.close()

# delimiter和lineterminator关键字参数
csvFile = open('example.csv', 'w', newline='')
csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
csvWriter.writerow(['apples', 'oranges', 'grapes'])
csvWriter.writerow(['eggs', 'bacon', 'ham'])
csvFile.close()