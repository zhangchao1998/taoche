# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TaocheItem(scrapy.Item):
    name = scrapy.Field()
    spsj = scrapy.Field()
    gls = scrapy.Field()
    address = scrapy.Field()
    money = scrapy.Field()
    pl = scrapy.Field()

