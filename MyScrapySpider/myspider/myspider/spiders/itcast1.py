# -*- coding: utf-8 -*-
import scrapy
import logging


class Itcast1Spider(scrapy.Spider):
    name = 'itcast1'
    allowed_domains = ['baidu.com']
    start_urls = ['https://www.baidu.com/']

    def parse(self, response):
        for i in range(10):
            item = {}
            item["come_from"] = "itcast1"
            logging.warning(item)

        pass