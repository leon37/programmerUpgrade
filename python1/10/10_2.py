import traceback
import os

def spam():
    bacon()

def bacon():
    raise Exception('This is the error message.')

try:
    spam()
except:
    os.chdir('./python1/10')
    errorFile = open('./errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to errorInfo.txt.')