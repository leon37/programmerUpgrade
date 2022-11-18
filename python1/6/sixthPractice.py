tableData = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
]


def printTable(table):
    lineMaxLen = []
    for line in tableData:
        max = 0
        for word in line:
            max = len(word) if len(word) > max else max
        lineMaxLen.append(max)
    lenRow = len(tableData)
    lenColumn = len(tableData[0])    
    for i in range(lenColumn):
        for j in range(lenRow):
            print(table[j][i].rjust(lineMaxLen[j]),end=' ')
        print('\n')


printTable(tableData)
