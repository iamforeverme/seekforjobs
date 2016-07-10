# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.exceptions import DropItem
import time,re
from time import mktime
from datetime import datetime


def salary_normalize(salary_str):
    match_salary = re.compile(r"[\d,Kk]+")
    if salary_str == "":
        return 0
    else:
        ls = match_salary.findall(salary_str)

        def contain_str(item_list, content_str):
            for item in item_list:
                if item in content_str:
                    return True
            return False

        def remove_useless(item_str):
            if item_str=='k' or item_str==',':
                return False
            return True
        ls=filter(remove_useless,ls)
        if ls:
            # unify format
            for i in range(len(ls)):
                ls[i] = ls[i].replace('k', '000')
                ls[i] = ls[i].replace('K', '000')
                ls[i] = ls[i].replace(',', '')
                ls[i] = int(ls[i])
                if ls[i] < 1000:
                    if contain_str(['-', 'to'], salary_str):
                        ls[i] = ls[i] * 1000
                    elif contain_str(['day', '.d', 'Daily', 'pd', 'PD'], salary_str):
                        ls[i] = ls[i] * 20 * 12
                    elif contain_str(['hour', '.h', '/h'], salary_str):
                        ls[i] = ls[i] * 20 * 8 * 12

            if len(ls) == 0:
                salary = salary_str
            elif len(ls) == 1:
                salary = ls[0]
                # salary_list.append(ls[0])
            elif len(ls) == 2:
                salary = int((ls[0] + ls[1]) / 2)
            else:
                salary_list = sorted(ls)
                salary = int((salary_list[-1] + salary_list[-2]) / 2)

            if salary<10000 or salary>1000000:
                return 0
            else:
                return salary
        else:
            return 0

class MongoPipeline(object):

    def __init__(self, mongo_uri, mongo_db,collection_name,mongo_port):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.collection_name = collection_name
        self.mongo_port = mongo_port

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_port=crawler.settings.get('MONGO_PORT'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items'),
            collection_name = crawler.settings.get('MONGODB_COLLECTION')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri,self.mongo_port)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if self.db[self.collection_name].find_one({"url": item["url"]}):
            raise DropItem("Duplicate mongo item found: %s" % item)
        item_dict=dict(item)
        item_dict["salary_index"]=salary_normalize(item_dict["salary_range"])
        item_dict["listing_date"]=datetime.fromtimestamp(mktime(time.strptime(item_dict["listing_date"], "%Y-%m-%dT%H:%M:%SZ")))
        self.db[self.collection_name].insert(item_dict)
        return item


class DuplicatesPipeline(object):
    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item['url'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item['url'])
            return item