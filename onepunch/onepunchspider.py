# -*-coding:utf-8-*-

import requests
from lxml import etree
import re
import json
import os


class OnePunchManSpider:
    def __init__(self, tieba_name):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/79.0.3945.88 Safari/537.36 "
        }
        self.tieba_name = tieba_name
        self.boutique_area_url = "https://tieba.baidu.com/f?kw={}&ie=utf-8&tab=good&cid=1&pn=0".format(tieba_name)
        self.post_url = "https://tieba.baidu.com"
        self.re_post_url = re.compile(r'href="(/p/\d*)" title="(.*?)"')  # 获取帖子url的正则
        self.re_pic_url = re.compile(r'src="(.*?)"')
        self.re_boutique_post_next_page_num = re.compile(r'<a href="(.*?)" class="next pagination-item "')

    def get_boutique_post_url(self, response_str):
        post_list = self.re_post_url.findall(response_str)
        return post_list

    def get_pic_url(self, pic_response_str):
        response_str_html = etree.HTML(pic_response_str)
        post_data = response_str_html.xpath("//div[@id='j_p_postlist']/div/@data-field")
        pic_num_list = []
        louzhu_id = json.loads(post_data[0])["author"]["user_id"]
        for i in post_data:
            user_id = json.loads(i)["author"]["user_id"]
            if user_id == louzhu_id:
                str1 = json.loads(i)["content"]["content"]
                pic_num_list += re.findall(r'src="(.*?.jpg)"', str1)
        return pic_num_list

    def get_next_page_num(self, response_str):
        url = self.re_boutique_post_next_page_num.findall(response_str)
        if url:
            return url[0]

    def get_next_pic_page_num(self, response_str):
        pic_html = etree.HTML(response_str)
        next_pic_page_url = pic_html.xpath("//a[text()='下一页']/@href")
        if next_pic_page_url:
            return self.post_url + next_pic_page_url[0]

    def save_pic(self, pic_url_list, path):

        for i in pic_url_list:
            pic_name = path + '/' + str(pic_url_list.index(i))
            pic_response = requests.get(i, headers=self.headers)
            with open(pic_name, "wb") as f:
                f.write(pic_response.content)

    def analyze_post_list(self, post_list):
        need_post_list = []
        for i in post_list:
            if re.search('二人小组', i[1]):
                need_post_list.append(i)
            elif re.search('不良漢化', i[1]):
                need_post_list.append(i)
            elif re.search('超市特卖', i[1]):
                need_post_list.append(i)
            elif re.search('个人汉化', i[1]):
                need_post_list.append(i)
        return need_post_list

    def get_post_url(self, need_post_list):
        return {i[1]: self.post_url + i[0] + '?see_lz=1' for i in need_post_list}

    def get_pic_url_list(self, post_url):
        pic_url_list = []
        while post_url:
            pic_response = requests.get(post_url, headers=self.headers)
            pic_response_str = pic_response.content.decode()
            pic_url_list += self.get_pic_url(pic_response_str)
            post_url = self.get_next_pic_page_num(pic_response_str)
        return pic_url_list

    def mkdir(self, path):
        # 去除首位空格
        path = path.strip()
        # 去除尾部 \ 符号
        path = path.rstrip("\\")
        # 判断路径是否存在
        # 存在     True
        # 不存在   False
        isExists = os.path.exists(path)
        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            # 创建目录操作函数
            os.makedirs(path)
            print
            path + ' 创建成功'
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            print
            path + ' 目录已存在'
            return False

    def run(self):
        # 1. 获取精品区帖子的url地址和标题
        boutique_area_page_url = self.boutique_area_url
        url = 1
        while url:
            response = requests.get(boutique_area_page_url, headers=self.headers)
            response_str = response.content.decode()
            post_list = self.get_boutique_post_url(response_str)  # 获取每一页的帖子的标题和url地址
            need_post_list = self.analyze_post_list(post_list)  # 简陋的筛选出想要的帖子
            post_url_dict = self.get_post_url(need_post_list)  # 加工成{“标题”：“url”}形式的字典

            for i in post_url_dict:
                print(i)
                save_path = "./" + self.tieba_name + "/" + i
                if not os.path.exists(save_path): # 判断目录是否存在
                    self.mkdir(save_path)  # 创建目录
                    pic_url_list = self.get_pic_url_list(post_url_dict[i]) # 获取图片url列表
                    print(len(pic_url_list))
                    print(pic_url_list)
                    self.save_pic(pic_url_list, save_path)  # 保存图片url列表

            url = self.get_next_page_num(response_str)  # 获取下一页url地址
            if url:
                boutique_area_page_url = 'https:' + url
            else:
                break


if __name__ == '__main__':
    onepunchmanspider = OnePunchManSpider("一击男")
    onepunchmanspider.run()
