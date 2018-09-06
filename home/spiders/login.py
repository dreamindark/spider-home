 # -*- coding: utf-8 -*-
import scrapy


class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['www.123.com']
    start_urls = ['http://www.123.com/']

    def parse(self, response):
        pass
