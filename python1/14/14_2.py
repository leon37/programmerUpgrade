# 假设你有一个枯燥的任务，要删除几百CSV文件的第一行。
# 也许你会将它们送入一个自动化的过程，只需要数据，不需要每列顶部的表头。
# 可以在Excel中打开每个文件，删除第一行，并重新保存该文件，但这需要几个小时。
# 让我们写一个程序来做这件事。
# 该程序需要打开当前工作目录中所有扩展名为.csv的文件，读取CSV文件的内容，并除掉第一行的内容重新写入同名的文件。
# 这将用新的、无表头的内容替换CSV文件的旧内容。

import csv, os

os.chdir('python1\\14')
os.makedirs('headerRemoved', exist_ok=True)
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue
    csvFile = open(csvFilename, 'r')
    rows = []
    for row in csv.reader(csvFile):
        if csv.reader(csvFile).line_num == 1:
            continue
        rows.append(row)
    csvWriteFile = open(os.path.join('headerRemoved', csvFilename), 'w', newline='')
    csvWriter = csv.writer(csvWriteFile)
    for row in rows:
        csvWriter.writerow(row)
    csvWriteFile.close()
    


