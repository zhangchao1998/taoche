# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class TaochePipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient('localhost')
        self.db = self.client['taoche']
        self.car = self.db['car']
    def process_item(self, item, spider):
        self.car.insert(dict(item))
        return item
