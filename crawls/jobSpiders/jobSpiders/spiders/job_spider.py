# encoding: utf-8
import scrapy
import re
import json
from selenium import webdriver

from ..items import JobspidersItem
from scrapy.utils.response import open_in_browser
from scrapy.shell import inspect_response


class JobSpider(scrapy.Spider):
    name = "jobSpiders"
    allowed_domains = ["http://www.seek.com.au"]
    keyWord = "python"
    paraDict  = {
       "displaySuburb": "",
       "searchFrom": "active+filters+clear+all+locations",
       "companyID": "",
       "salaryFrom": "0",
       "graduateSearch": "false",
       "seoSuburb": "",
       "advertiserGroup": "",
       "keywords": keyWord,
       "occupation": "",
       "isAreaUnspecified": "false",
       "searchType": "",
       "area": "",
       "advertiserID": "",
       "location": "",
       "whereIsDirty": "false",
       "whereId": "",
       "sortMode": "KeywordRelevance",
       "nation": "",
       "salaryTo": "999999",
       "salaryType": "annual",
       "workType": "0",
       "industry": "",
       "dateRange": "999",
       "where": "",
       "page": "1",
    }
    para = ""
    for key in paraDict:
        para = para + key + "=" + paraDict[key] + "&"



    start_urls = [
        r"http://www.seek.com.au/jobs/#" +para,
    ]
    count = 3

    def __init__(self):
        scrapy.Spider.__init__(self)
        # self.verificationErrors = []
        # self.webdriver = webdriver.Chrome()


    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        inspect_response(response, self)
        # for selector in response.selector.xpath('//div/a'):
        #     pageIndex = selector.xpath("text()").extract()
        #     if( u'\u4e0b\u4e00\u9875' in pageIndex):
        #         url = response.urljoin(selector.xpath("@href").extract()[0])
        #         yield scrapy.Request(url, callback=self.parse)
        #
        # for href in response.selector.xpath('//li/a/@href').extract():
        #     url = response.urljoin(href)
        #     yield scrapy.Request(url, callback=self.parse_dir_contents)