# -*- coding: utf-8 -*-
import scrapy


class JiandanSpider(scrapy.Spider):
    name = 'jiandan'
    allowed_domains = ['http://jandan.net/ooxx']
    start_urls = ['http://http://jandan.net/ooxx/']

    def parse(self, response):
        pass
