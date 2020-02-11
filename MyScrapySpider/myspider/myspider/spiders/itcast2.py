# -*- coding: utf-8 -*-
import scrapy


class Itcast2Spider(scrapy.Spider):
    name = 'itcast2'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        pass
