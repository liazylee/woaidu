#!/usr/bin/env python
# coding=utf-8
import pymongo

__auther__ = 'liazylee'
# connect='li233111@gmail.com'
# @Time    : 6/9/19 12:49 AM
# @FileName: mongo_database.py
# @Software: PyCharm
# @project: woaidu


class MongoDBConnect:

    def __init__(self):
        clint = pymongo.MongoClient('localhost', 27017)
        db = clint['woaidu']
        self.woaodu = db['woaidu_data']
        self.woaodu.create_index('book_name')

mongoConnection=MongoDBConnect()