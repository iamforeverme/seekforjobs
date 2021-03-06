# encoding: utf-8
import scrapy
import re

from ..items import JobspidersItem
from scrapy.utils.response import open_in_browser
from scrapy.shell import inspect_response
import logging
from math import ceil
import json

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


def get_item(key, element):
    if key in element:
        return element[key]
    else:
        return ""

class JobSpider(scrapy.Spider):
    name = "jobSpiders"
    #allowed_domains = ["http://www.seek.com.au"]
    para_str="callback=jQuery18203872003472526937_1466515875404&keywords=python&companyProfileStructuredDataId=&hirerId=&hirerGroup=&page=4&classification=&subclassification=&graduateSearch=false&whereId=&location=&nation=&area=&isAreaUnspecified=false&worktype=&salaryRange=0-999999&salaryType=annual&dateRange=999&sortMode=KeywordRelevance&engineConfig=&usersessionid=ct5yl5ihcm0m0kefdw4wueld&userid=1f6d0e23-60f6-452f-a573-c30c25d582dd&eventCaptureSessionId=94f0ea85-05e7-4d07-a93d-5225b6a6d933&userqueryid=202872875205887903&include=expanded&siteKey=AU-Main&seekSelectAllPages=true&hadPremiumListings=false&_=1466518595406"

    root_urls = r"https://jobsearch-api.cloud.seek.com.au/search?&"
    count = 1

    def __init__(self, *a, **kw):
        super(JobSpider, self).__init__(*a, **kw)
        self.para_dict={}
        for equation in self.para_str.split("&"):
            self.para_dict[equation.split("=")[0]]=equation.split("=")[1]
        if "n_crawls" in kw.keys():
            self.n_crawls=kw["n_crawls"]
            self.crawl_num = kw["crawl_num"]
            self.key_word=kw["key_word"]
            self.para_dict["keywords"] = self.key_word
            self.para_dict["page"]=str(self.crawl_num)
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
        content_str = response.body[response.body.find('('):response.body.rfind(')')].strip('()')
        content_json = json.loads(content_str)
        for element in content_json['data']:
            item = JobspidersItem()
            item['title'] = get_item('title',element)
            url = element['tracking']['clickUrl']
            if isinstance(url, basestring):
                userqueryid=url.split('?')[1].split('&')[0].split('=')[1]
                job_id=url.split('?')[1].split('&')[2].split('=')[1]
                item['url']=r"http://www.seek.com.au/job/{0}?pos=19&type=standard&engineConfig=&userqueryid={1}&tier=no_tier&whereid=".format(job_id,userqueryid)
            item['salary_range'] = get_item('salary',element)
            item['listing_date'] = get_item('listingDate',element)
            item['location'] = get_item('locationWhereValue',element)
            item['sublocation'] = get_item('suburb',element)
            yield item
        n_total=int(content_json['totalCount'])
        n_single_page = len(content_json['data'])
        n_pages = int(ceil(float(n_total) / n_single_page))
        cur_page = self.para_dict["page"]
        next_page = int(cur_page) + int(self.n_crawls)
        # inspect_response(response, self)
        if next_page<n_pages:
            self.para_dict["page"] = str(next_page)
            next_url = self.root_urls + serialize(self.para_dict)
            yield scrapy.Request(next_url,callback=self.parse,
                                  dont_filter=True,
                                  meta={
                                      'PhantomJS': True,
                                      'keywords': self.key_word,
                                  })
        # article_root = response.selector.xpath('//article')
        # for article in article_root:
        #     title_root = article.css('.job-title')
        #     title_text = title_root.xpath('.').extract()[0]
        #     # fetch job title
        #     raw_str = re.search(r'>[\d\D]+</a>', title_text).group(0)
        #     item = JobspidersItem()
        #     item['title'] = re.sub(r'<.*?>', '', raw_str).strip(">")
        #     item['url'] = response.urljoin(title_root.xpath('@href').extract()[0])
        #     item['salary_range'] = get_item(article.css('.salary-range').xpath('text()').extract())
        #     item['listing_date'] = get_item(article.css('.listing-date').xpath('text()').extract())
        #     item['location'] = get_item(article.css('.location').xpath('text()').extract())
        #     item['sublocation'] = get_item(article.css('.sublocation').xpath('text()').extract())
        #     yield item
        # cur_page=get_item(response.selector.css('.current-page').xpath('./span/text()').extract())
        # n_total = response.selector.css('.animation').xpath('text()').extract()[0]
        # n_total = ''.join([num for num in n_total if num!= ','])
        # n_single_page = len(response.selector.xpath('//article'))
        # n_pages = int(ceil(float(n_total)/n_single_page))
        # next_page=int(cur_page)+int(self.n_crawls)
        # if next_page<n_pages:
        #     para_dict = self.para_dict
        #     para_dict["page"] = str(next_page)
        #     next_url = self.root_urls + serialize(para_dict)
        #     yield scrapy.Request(next_url,callback=self.parse,
        #                           dont_filter=True,
        #                           meta={
        #                               'PhantomJS': True,
        #                               'keywords': self.key_word,
        #                           })
        #inspect_response(response, self)
