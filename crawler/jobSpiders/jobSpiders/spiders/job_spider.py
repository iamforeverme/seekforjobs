# encoding: utf-8
import scrapy
import re

from ..items import JobspidersItem
from scrapy.utils.response import open_in_browser
from scrapy.shell import inspect_response
import logging
from math import ceil

logger = logging.getLogger()


def get_item(src):
    if len(src) != 0:
        return src[0]
    else:
        return ''


def serialize(para_dict):
    para = ""
    for key in para_dict:
        para = para + key + "=" + para_dict[key] + "&"
    return para


class JobSpider(scrapy.Spider):
    name = "jobSpiders"
    #allowed_domains = ["http://www.seek.com.au"]
    para_dict={
       "displaySuburb": "",
       "searchFrom": "active+filters+clear+all+locations",
       "companyID": "",
       "salaryFrom": "0",
       "graduateSearch": "false",
       "seoSuburb": "",
       "advertiserGroup": "",
       "keywords": "",
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
    root_urls = r"http://www.seek.com.au/jobs/#"
    count = 1

    def __init__(self, *a, **kw):
        super(JobSpider, self).__init__(*a, **kw)

        if "n_crawls" in kw.keys():
            self.n_crawls=kw["n_crawls"]
            self.crawl_num = kw["crawl_num"]
            self.key_word=kw["key_word"]
            self.para_dict["keywords"]=self.key_word
            self.start_urls=[
                self.root_urls + serialize(self.para_dict),
            ]
        else:
            self.n_crawls = 1
            self.crawl_num = 1
            self.key_word = "python"
        self.para_dict["keywords"] = self.key_word
        self.start_urls = [
            self.root_urls + serialize(self.para_dict),
        ]


#     headStr=r"""Host: www.seek.com.au
# Connection: keep-alive
# Cache-Control: max-age=0
# Upgrade-Insecure-Requests: 1
# User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
# Accept-Encoding: gzip, deflate, sdch
# Accept-Language: zh-CN,zh;q=0.8"""
#     def start_requests(self):
#         # header ={}
#         # for line in self.headStr.splitlines():
#         #     header[line.split(":")[0]] = line.split(":")[-1]
#         for url in self.start_urls:
#             yield scrapy.Request(url, self.parse,
#                                  #headers=header,
#                                  meta={
#                                     'PhantomJS': self.driver,
#                                     'keywords': self.keyWord,
#                                     }
#             )

    def make_requests_from_url(self,url):
        print("make_requests_from_url :"+self.key_word)
        return scrapy.Request(url, self.parse,
                                 meta={
                                    'PhantomJS': True,
                                    'keywords': self.key_word,
                                    })

    def parse(self,response):
        "In the whole process, this function will be triggered once"
        n_total = response.selector.css('.animation').xpath('text()').extract()[0]
        n_total = ''.join([num for num in n_total if num!= ','])
        n_single_page = len(response.selector.xpath('//article'))
        n_pages = int(ceil(float(n_total)/n_single_page))
        for page in range(5,6):#range(self.crawl_num,n_pages+1,self.n_crawls):
            para_dict = self.para_dict
            para_dict["page"] = str(page)
            next_url = self.root_urls + serialize(para_dict)
            yield scrapy.Request(next_url,callback=self.parse_jobs,
                                  dont_filter=True,
                                  meta={
                                      'PhantomJS': True,
                                      'keywords': self.key_word,
                                  })
        #inspect_response(response, self)

    def parse_jobs(self, response):
        #inspect_response(response, self)
        print("parse items :" + self.key_word)
        article_root = response.selector.xpath('//article')
        for article in article_root:
            title_root = article.css('.job-title')
            title_text = title_root.xpath('.').extract()[0]
            # fetch job title
            raw_str = re.search(r'>[\d\D]+</a>', title_text).group(0)
            item = JobspidersItem()
            item['title'] = re.sub(r'<.*?>', '', raw_str).strip(">")
            item['url'] = response.urljoin(title_root.xpath('@href').extract()[0])
            item['salary_range'] = get_item(article.css('.salary-range').xpath('text()').extract())
            item['listing_date'] = get_item(article.css('.listing-date').xpath('text()').extract())
            item['location'] = get_item(article.css('.location').xpath('text()').extract())
            item['sublocation'] = get_item(article.css('.sublocation').xpath('text()').extract())
            yield item