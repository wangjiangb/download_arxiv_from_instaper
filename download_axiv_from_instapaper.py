from instapaper import Instapaper as ipaper
import json
import os


with open('./account_info.json') as f:
    account_info = json.loads(f.read())

i = ipaper(account_info['api_key'], account_info['api_secret'])
i.login(account_info['email'], account_info['password'])
marks = i.bookmarks(limit=30)
urls = []
for m in marks:
    if m.url.find('arxiv') > 0:
        urls.append(m.url)
        print("Adding {}".format(m.url))
        m.archive()

cmd = 'getpaper -d /home/jiangwang/Dropbox/Papers/ -p '
for u in urls:
    cmd += (u + ' ')
print(cmd)
os.system(cmd)
