import imapclient

imapObj = imapclient.IMAPClient('imap.qq.com', ssl=True)
print(imapObj)