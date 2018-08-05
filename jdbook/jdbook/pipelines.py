# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import redis
class JdbookPipeline(object):
    def process_item(self, item, spider):
        return item
class RedisPipline:
    def openspider(self,spider):
        self.dbhost = spider.settings.get('REDIS_HOST','localhost')
        self.dbport = spider.settings.get('REDIS_PORT',6379)
        self.dbindex = spider.settings.get('REDIS_DB_INDEX',0)
        self.dbconn = redis.StrictRedis(host=self.dbhost,port=self.dbport,db = self.dbindex)
        self.item_i = 0

    def closespider(self):
        self.dbconn.connection_pool.disconnect()

    def process_item(self,item):
        self.insertdb(item)
        return item
    def insertdb(self,item):
        self.item_i += 1
        self.dbconn.hmset('book:%s'%self.item_i,item)