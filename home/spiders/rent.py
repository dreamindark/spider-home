# -*- coding: utf-8 -*-
import scrapy
import random
from home.items import HomeItem
from scrapy_redis.spiders import RedisSpider
class RentSpider(RedisSpider):
    name = 'rent'
    redis_key = 'home:rent'
    # allowed_domains = ['hz.zu.anjuke.com']
    # start_urls = ['http://hz.zu.anjuke.com/fangyuan/yuhang/x2//']

    def __init__(self,*arg,**kwargs):
        domain = kwargs.pop('domain','')
        self.allowed_domain = filter(None,domain.split(','))
        super(RentSpider,self).__init__(*arg,**kwargs)

    def parse(self, response):
        # // div[@class ="zu-itemmod"]
        infos = response.xpath('//div[@class ="zu-info"]').xpath("..")

        for info in infos:
            larger = info.xpath('.//p[@class="details-item tag"]/text()').extract()
            money = info.xpath('.//div[@class="zu-side"]/p/strong/text()').extract_first()
            size = larger[0].strip()
            area = larger[1].strip()

            item = HomeItem()
            item["money"] = money
            item["size"] = size
            item["area"] = area

            yield item
        next_page = response.xpath('//a[@class="aNxt"]')

        if next_page:
            yield response.follow(next_page[0],callback=self.parse)



