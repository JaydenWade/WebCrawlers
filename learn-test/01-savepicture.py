# -*-coding:utf-8-*-
import requests


URL = "https://upload.cc/i1/2020/01/05/kjZavr.jpg"
r = requests.get(URL)
with open ('c.jpg', 'wb') as f:
    f.write(r.content)
