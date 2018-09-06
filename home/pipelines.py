# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.contrib.exporter import JsonItemExporter
from pymongo import MongoClient
import pymysql
import pymongo

class HomePipeline(object):
    def process_item(self, item, spider):

        return item

# class MySQLPipelines(object):
#     def __init__(self):
#         self.coon = pymysql.connect(host='127.0.0.1',user='root',password='19961213',
#                                     db='home',charset='utf8')
#         self.cursor = self.coon.cursor()
#
#     def process_item(self,item,spider):
#         sql = "insert into home.rent(size,area,money) values(%s,%s,%s)"
#
#         self.cursor.execute(sql,(item['size'],item['area'],item['money']))
#         self.coon.commit()
#         return item
#     def close_spider(self,spider):
#
#         self.cursor.close()
#         self.coon.close()
#
# class MongoDBPipeline(object):
#     def __init__(self):
#         self.client = pymongo.MongoClient(host='127.0.0.1',port=27017)
#         self.db = self.client['home']
#         self.coll = self.db['rent']
#
#     def process_item(self,item,spider):
#         dict_item = dict(item)
#         self.coll.insert(dict_item)
#         return item
#     def close_spider(self,spider):
#         self.client.close()










