import requests


r = requests.get("https://upload.cc/i1/2020/01/05/kjZavr.jpg")
with open ('b.jpg', 'wb') as f:
    f.write(r.content)
