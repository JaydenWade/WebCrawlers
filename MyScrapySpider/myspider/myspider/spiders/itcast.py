# -*- coding: utf-8 -*-
import scrapy
import logging

logger = logging.getLogger(__name__)

class ItcastSpider(scrapy.Spider):
    name = 'itcast'  # 爬虫名
    allowed_domains = ['itcast.cn'] # 允许爬虫的范围
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml'] # 最开始请求的url地址

    def parse(self, response):
        # 处理start_urls地址对应的响应
        # ret1 = response.xpath("//div[@class='tea_con']//h3/text()").extract()
        # print(ret1)

        # 分组
        # li_list = response.xpath("//div[@class='tea_con']//li")
        # for li in li_list:
        #     item = {}
        #     # b = li.xpath(".//h3/text()")
        #     # print(b)
        #     # a = li.xpath(".//h3/text()").extract()
        #     # print(a)
        #     item["name"] = li.xpath(".//h3/text()").extract_first()
        #     item["title"] = li.xpath(".//h4/text()").extract()[0]
        #     # print(item)
        #     yield item
        for i in range(10):
            item = {}
            item["come_from"] = "itcast1"
            logger.warning(item)
            yield item
