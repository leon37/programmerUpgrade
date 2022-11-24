import requests

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')

if res.status_code == requests.codes.ok:
    playFile = open('./python1/11/RemeoAndJuliet.txt','wb')
    for chunk in res.iter_content(100000):
        playFile.write(chunk)

    playFile.close()