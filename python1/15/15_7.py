'''
author:leon
project:programmerUpgrade
date:2022/12/2
email:13368447@qq.com
'''
<<<<<<< HEAD
# 在第11章，你编写了一个程序，从XKCD网站下载所有的XKCD漫画。
# 这是一个单线程程序：它一次下载一幅漫画。
# 程序运行的大部分时间，都用于建立网络连接来开始下载，以及将下载的图像写入硬盘。
# 如果你有宽带因特网连接，单线程程序并没有充分利用可用的带宽。
import requests
import os
import bs4
import threading


def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        print('Downloading page http://xkcd.com/%s' % (urlNumber))
        res = requests.get('http://xkcd.com/%s' % (urlNumber))
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text)
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = comicElem[0].get('src')
            # Download the image.
            print('Downloading image %s...' % (comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()

            imageFile = open(os.path.join(
                'xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()


downloadThreads = []
for i in range(0, 1400, 100):
    downloadThread = threading.Thread(target=downloadXkcd, args=(i, i+99))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# Wait for all threads to end.
for downloadThread in downloadThreads:
    downloadThread.join()

print('Done.')
=======
>>>>>>> d08fbce5eaf32adba5ced747e8bd376a4efe5519
