# -*-coding:utf-8-*-

# -*-coding:utf-8-*-

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/79''.0.3945.88 Safari/537.36',
}
cookies = ""
cookies = {i.split("=")[0]: i.split("=")[1] for i in cookies.split("; ")}

r = requests.get("https://wrmyx.com/plus/downlink.php?aid=474", headers=headers, cookies=cookies)

with open('wrmyxlianjie3.html', 'w', encoding='utf-8') as f:
    f.write(r.content.decode())
