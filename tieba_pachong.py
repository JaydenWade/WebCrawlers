# -*-coding:utf-8-*-
import requests


# headers = {
#     'ser-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                  'AppleWebKit/537.36 (KHTML, like Gecko) '
#                  'Chrome/79''.0.3945.88 Safari/537.36'
#             }
#
# tieba_name = input("input tieba name:")
#
# for page_num in range(0,1001,50):
#     url = 'https://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}'.format(tieba_name, page_num)
#     # print(page_num)
#     r = requests.get(url, headers=headers)
#     print(r.request.url)

class TiebaSpider:
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.url = 'https://tieba.baidu.com/f?kw=' + tieba_name + '&ie=utf-8&pn={}'
        self.headers = {
            'ser-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/79''.0.3945.88 Safari/537.36'
        }

    def get_url_list(self):  # make url list
        # url_list = []
        # for i in range(1001):
        #     url_list.append(self.url.format(i*50))
        # return url_list
        return [self.url_list.format(i * 50) for i in range(1000)]

    def parse_url(self, url):  # send requests, get response
        print(url)
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def save_html(self, html_str, page_num):  # save html string
        file_path = "{}-{}.html".format(self.tieba_name, page_num)
        with open(file_path, "w", encoding="utf-8") as f:  # lol-pagenum.html
            f.write(html_str)

    def run(self):  # achieve main logic
        # 1. make url list
        url_list = self.get_url_list()
        # 2. ergodic, send request and get response
        for url in url_list:
            html_str = self.parse_url(url)
            # 3. save
            page_num = url_list.index(url) + 1
            self.save_html(html_str, page_num)


if __name__ == '__main__':
    tiebaspider = TiebaSpider("lol")
    tiebaspider.run()
