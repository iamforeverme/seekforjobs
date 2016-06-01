# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobspidersItem(scrapy.Item):
    company = scrapy.Field()
    position = scrapy.Field()
    salary = scrapy.Field()
