# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector, HtmlXPathSelector
from scrapy.http import HtmlResponse


class JiandanSpider(scrapy.Spider):
    name = 'jiandan'
    allowed_domains = ['jandan.net']
    start_urls = ['http://jandan.net/ooxx/']

    def parse(self, response):
        hxs = Selector(response=response).xpath("//li[re:test(@id,'comment-\d+')]")
        # hxs = Selector(response=response).xpath('//li[re:test(@id,"comment-\d+")]')


        print(hxs,type(hxs))
        # for i in hxs:
        imgs = hxs.xpath(".//img/@src").extract()

        print(imgs)

