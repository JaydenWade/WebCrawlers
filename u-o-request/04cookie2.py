# -*-coding:utf-8-*-

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/79''.0.3945.88 Safari/537.36',
    'Cookie': ""
}

r = requests.get("https://wrmyx.com/plus/downlink.php?aid=474", headers=headers)

with open('wrmyxlianjie.html', 'w', encoding='utf-8') as f:
    f.write(r.content.decode())
