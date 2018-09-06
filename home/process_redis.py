from redis import Redis
import pymysql
import time
import json
import settings

class RedisPipeline(object):
    def __init__(self):
        self.coon=pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='19961213',
            port=3306,
            db='home'
        )
        self.cursor = self.coon.cursor()
        self.rds = Redis('127.0.0.1',6379)
    def process_item(self):
        while True:
            self.rds.lpush('home:rent http://hz.zu.anjuke.com/fangyuan/yuhang/x2//',1)
            _, data = self.rds.blpop(settings.REDIS_ITEMS_KEY)
            print(data)
            item = json.loads(data.decode('utf-8'))
            sql = "insert into home:rent(size,area,money) values (%s,%s,%s)"
            self.cursor.execute(sql,(item['size'],item['area'],item['money']))
            self.coon.commit()
    def close(self):
        self.cursor.close()
        self.coon.close()

redis_pipelie = RedisPipeline()
redis_pipelie.process_item()
redis_pipelie.close()




