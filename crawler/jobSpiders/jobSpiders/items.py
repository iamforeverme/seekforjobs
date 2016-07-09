# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobspidersItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    salary_range = scrapy.Field()
    salary_index = scrapy.Field()
    listing_date = scrapy.Field()
    location = scrapy.Field()
    sublocation = scrapy.Field()
