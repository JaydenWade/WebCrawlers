# -*-coding:utf-8-*-

# -*-coding:utf-8-*-

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/79''.0.3945.88 Safari/537.36',
    # 'Cookie': "UM_distinctid=16ecef6fda066b-03c05379755d2-7711b3e-1fa400-16ecef6fda1a7a; "
    #           "PHPSESSID=ae790a4661cfdad2d0b7d9c1f9b3701b; DedeUserID=11536; DedeUserID__ckMd5=73628e04090b49b1; "
    #           "DedeLoginTime=1579412498; DedeLoginTime__ckMd5=d7d3c5315753820c; "
    #           "CNZZDATA1275365794=1667788893-1575604041-https%253A%252F%252Fwww.wrmyx.com%252F%7C1579412528; "
    #           "CNZZDATA1256801056=1191899815-1575604041-https%253A%252F%252Fwww.wrmyx.com%252F%7C1579412528 "
}
cookies = "UM_distinctid=16ecef6fda066b-03c05379755d2-7711b3e-1fa400-16ecef6fda1a7a; PHPSESSID=ae790a4661cfdad2d0b7d9c1f9b3701b; DedeUserID=11536; DedeUserID__ckMd5=73628e04090b49b1; DedeLoginTime=1579412498; DedeLoginTime__ckMd5=d7d3c5315753820c; CNZZDATA1275365794=1667788893-1575604041-https%253A%252F%252Fwww.wrmyx.com%252F%7C1579412528; CNZZDATA1256801056=1191899815-1575604041-https%253A%252F%252Fwww.wrmyx.com%252F%7C1579412528"
cookies = {i.split("=")[0]: i.split("=")[1] for i in cookies.split("; ")}

r = requests.get("https://wrmyx.com/plus/downlink.php?aid=474", headers=headers, cookies=cookies)

with open('wrmyxlianjie3.html', 'w', encoding='utf-8') as f:
    f.write(r.content.decode())
