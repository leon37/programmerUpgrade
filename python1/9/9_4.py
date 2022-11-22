# 假定你的老板用电子邮件发给你上千个文件，文件名包含美国风格的日期（MM-DD-YYYY），
# 需要将它们改名为欧洲风格的日期（DD-MM-YYYY）。
# 手工完成这个无聊的任务可能需要几天时间！让我们写一个程序来完成它。

import re
import os
import shutil

datePattern = re.compile(r'''(
    (.*?)               # (1)
    ((0|1)?\d)-         # (2(3))    
    ((0|1|2|3)?\d)-     # (4(5))
    ((19|20)\d\d)       # (6(7))
    (.*?)$              # (8)
)''', re.VERBOSE)

for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)
    if not mo:
        continue

    beforePart = mo.group[1]
    monthPart = mo.group[2]
    dayPart = mo.group[4]
    yearPart = mo.group[6]
    afterPart = mo.group[8]

    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart
    originName = os.path.join(os.path.abspath('.'), amerFilename)
    newName = os.path.join(os.path.abspath('.'), euroFilename)

    shutil.move(originName, newName)
