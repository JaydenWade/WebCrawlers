# -*-coding:utf-8-*-
import json
import requests
import sys

sourceText_string = sys.argv

headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Mobile Safari/537.36"}

post_data = {
"from": "0",
"to": "1",
"sourceText": "{}".format(sourceText_string[1]),
"type": "1",
"latitude": "1",
"longitude": "1",
"platform": "H5"

}

post_url ="https://m.fanyi.qq.com/translate"

r = requests.post(post_url,data=post_data,headers=headers)

# print(r.content.decode())
dict_ret = json.loads(r.content.decode())

ret = dict_ret["targetText"]
print("the result is:", ret)


