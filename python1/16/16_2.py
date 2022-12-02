import smtplib

FIRST_EMAIL = '13368447@qq.com'
SECOND_EMAIL = '2199038610@qq.com'
MY_SECRET_PASSWORD = '***********'
smtpObj = smtplib.SMTP_SSL('smtp.qq.com', 465)
print(type(smtpObj))
# print(smtpObj.ehlo())
print(smtpObj.login(FIRST_EMAIL, MY_SECRET_PASSWORD))
print(smtpObj.sendmail(FIRST_EMAIL, SECOND_EMAIL,
'Subject:\n So long.\nDear Alice, so long and thanks for all the fish. Sincerely, Bob'))
print(smtpObj.quit())