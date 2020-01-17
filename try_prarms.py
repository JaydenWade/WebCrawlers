# -*-coding:utf-8-*-
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
# p = {'query': 'huya'}
# url_temp = "https://www.sogou.com/web?"
#
# r = requests.get(url_temp, headers=headers, params=p)
#
# print(r.status_code)
# print(r.request.url)

url = "https://www.sogou.com/web?query={}".format("huya")
r = requests.get(url, headers=headers)

print(r.status_code)
print(r.request.url)


