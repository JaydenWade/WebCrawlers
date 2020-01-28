# -*-coding:utf-8-*
# Done is better than perfect
import requests
import re
from lxml import etree
import time
import json


class GameSpider:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/79''.0.3945.88 Safari/537.36',
            'Cookie': "UM_distinctid=16ecef6fda066b-03c05379755d2-7711b3e-1fa400-16ecef6fda1a7a; DedeUserID=11536; "
                      "DedeUserID__ckMd5=73628e04090b49b1; "
                      "CNZZDATA1275365794=1667788893-1575604041-https%253A%252F%252Fwww.wrmyx.com%252F%7C1579756296; "
                      "CNZZDATA1256801056=1191899815-1575604041-https%253A%252F%252Fwww.wrmyx.com%252F%7C1579756297 "
        }
        self.page_url = "https://wrmyx.com/index_{}.html"
        self.download_url = "https://wrmyx.com/plus/downlink.php?aid={}"

    def get_game_url(self, url, headers):
        game_page_response = requests.get(url, headers=headers)
        game_page_response_str = game_page_response.content.decode()
        html = etree.HTML(game_page_response_str)
        game_url_temp_list = html.xpath("//article/header/h1/a/@href")
        game_name_list = html.xpath("//article/header/h1//text()")
        return game_name_list, [url + i for i in game_url_temp_list]

    def get_download_list(self, game_url):
        # 1. from game_url_list get the game_id
        num = re.findall(r"/(\d+).", game_url)
        # 2. use game_id make a download url
        return self.download_url.format(num[0])

    def get_download_data(self, download_url, headers):
        download_data_response = requests.get(download_url, headers=headers)
        download_data_response_str = download_data_response.content.decode()
        html = etree.HTML(download_data_response_str)
        down_data_link = html.xpath("//tr/td/a/@href")
        down_data = html.xpath("//tr/td/text()")
        return down_data_link, down_data

    def run(self):  # main logic
        # 1.get the game url
        # 1.1 get the next page url
        page_num = 0
        while page_num <= 74:
            time.sleep(5)
            page_num += 1
            page_url = self.page_url.format(page_num)
            print(page_num)
            print(page_url)
            # 1.2 from the page_url get first pages's games' url
            game_name_list, game_url_list = self.get_game_url(page_url, self.headers)
            # 1.3 get the download url
            for i in game_url_list:
                download_url = self.get_download_list(i)
                name_index = game_url_list.index(i)
                name = game_name_list[name_index]
                # 2.request the url for data
                # 2.1 request the game url for name
                # 2.2 request the down url for download address
                download_data_link, down_data = self.get_download_data(download_url, self.headers)
                # 3.save the name of games and download address
                with open("game_down_link.txt", "a", encoding="utf-8") as f:
                    f.write(name)
                    f.write("\n\r")
                    f.write(json.dumps(down_data, ensure_ascii=False))
                    f.write("\n\r")
                    f.write(json.dumps(download_data_link, ensure_ascii=False))
                    f.write("\n\r")


if __name__ == '__main__':
    game_spider = GameSpider()
    game_spider.run()
