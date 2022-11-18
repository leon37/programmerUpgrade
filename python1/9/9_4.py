# 假定你的老板用电子邮件发给你上千个文件，文件名包含美国风格的日期（MM-DD-YYYY），
# 需要将它们改名为欧洲风格的日期（DD-MM-YYYY）。
# 手工完成这个无聊的任务可能需要几天时间！让我们写一个程序来完成它。

import re
import os
import shutil

dataPattern = re.compile(r'''(
    (.*?)
    ((0|1)?\d)-
    ((0|1|2|3)?\d)-
    ((19|20)\d\d)
    (.*?)$
)''', re.VERBOSE)
