# -*-coding:utf-8-*-
import requests

proxies = {'http': 'http://114.226.244.141:9999'}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                 'AppleWebKit/537.36 (KHTML, like Gecko) '
                 'Chrome/79''.0.3945.88 Safari/537.36'
}

r = requests.get('http://www.baidu.com', headers=headers, proxies=proxies)

print(r.status_code)