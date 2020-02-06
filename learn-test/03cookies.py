# -*-coding:utf-8-*-
import requests

session = requests.session()
post_url = "https://acghgame.com/member.php?mod=logging&action=login"
post_data = {"username":"****************", "password":"*********"}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                 'AppleWebKit/537.36 (KHTML, like Gecko) '
                 'Chrome/79''.0.3945.88 Safari/537.36'
}
# use the session to send the post requests, the cookie will be save in session
session.post(post_url, data=post_data, headers=headers)

# the use the session to request the web which need to login
r = session.get("**********", headers=headers)