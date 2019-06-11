# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo as pymongo

from woaidu.untils.mongo_database import mongoConnection


class WoaiduPipeline(object):


    def process_item(self, item, spider):
        try:
            mongoConnection.woaodu.update_one({'book_name':item['book_name']}, {'$set': dict(item)}, upsert=True)
        except Exception as e:
            print(e)

