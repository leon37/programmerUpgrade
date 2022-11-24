import requests

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112eiei.txt')
try:
    res.raise_for_status()
except Exception as exc:
    print("There was a problem: %s" % exc)