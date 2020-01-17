# -*-coding:utf-8-*-
import requests

headers = {
    'ser-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                 'AppleWebKit/537.36 (KHTML, like Gecko) '
                 'Chrome/79''.0.3945.88 Safari/537.36'
}

data = {
"source":"auto",
"target": "zh",
"sourceText": "hola",
"qtv":"e1886386250e8e04",
"qtk": "YutIYbav37LDdbGR8jLsSBlqMkCyXRsrSRspGwOhdAw+ZS6aCMv4TI7nrnnEjNXJgFNoa8kInMDSYqILYFm23kb+SIN8NeNmOm5ifoj9UqwnMZZ0KbjzKdysGaU6BmEQo+9uqcT1AbNWQfALgvqduA==",
"sessionUuid": "translate_uuid1579249802033"

}

post_url = "https://fanyi.qq.com/api/translate"

r = requests.post(post_url, data=data, headers=headers)

print(r)

