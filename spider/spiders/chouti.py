# -*- coding: utf-8 -*-
import scrapy



class ChoutiSpider(scrapy.Spider):
    name = 'chouti'
    allowed_domains = ['dig.chouti.com']
    start_urls = ['http://dig.chouti.com/']

    def parse(self, response):
        print(111)
