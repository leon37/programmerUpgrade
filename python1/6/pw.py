#! python3
# pw.py - An insecure password locker program.

import sys
import pyperclip
PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] -copy account password')
    sys.exit()

account = sys.argv[1]
if account in PASSWORDS.keys():
    password = PASSWORDS[account]
    pyperclip.copy(password)
    print('The account ' + account+'\' password has copied to clipboard.')
else:
    print('There is no account named ' + account)