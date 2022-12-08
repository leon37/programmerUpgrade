'''
author:leon
project:programmerUpgrade
date:2022/12/8
email:13368447@qq.com
'''
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")

print('Give me two numbers, and I\'ll divide them.')
print("Enter 'q' to quit.")

while True:
    firstNumber = input('\nFirst number: ')
    if firstNumber == 'q':
        break
    secondNumber = input('\nSecond number:')
    if secondNumber == 'q':
        break

    try:
        answer = int(firstNumber) / int(secondNumber)
    except ZeroDivisionError:
        print("You can't devide by zero.")
    else:
        print(answer)
