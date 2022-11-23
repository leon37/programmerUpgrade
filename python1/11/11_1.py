'''
author:leon
project:programmerUpgrade
date:2022/11/23
email:13368447@qq.com
'''
import webbrowser
import sys
import pyperclip

# webbrowser.open('http://inventwithpython.com')
# 870 Valencia St, San Francisco, CA 94110

address = ''
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

if address:
    webbrowser.open('https://www.google.com/maps/place/{}'.format(address))