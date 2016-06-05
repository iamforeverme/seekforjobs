# encoding: utf-8
import scrapy
import re

from ..items import JobspidersItem
from scrapy.utils.response import open_in_browser
from scrapy.shell import inspect_response
import logging
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
    keyWord = "python"
    para_dict={
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
    root_urls = r"http://www.seek.com.au/jobs/#"

    start_urls=[
        root_urls + serialize(para_dict),
    ]
    count = 1

#     headStr=r"""Host: www.seek.com.au
# Connection: keep-alive
# Cache-Control: max-age=0
# Upgrade-Insecure-Requests: 1
# User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
# Accept-Encoding: gzip, deflate, sdch
# Accept-Language: zh-CN,zh;q=0.8"""
#     def start_requests(self):
#         header ={}
#         for line in self.headStr.splitlines():
#             header[line.split(":")[0]] = line.split(":")[-1]
#         for url in self.start_urls:
#             yield scrapy.Request(url, self.parse,
#                                  headers=header,
#                                  meta={
#                                     'PhantomJS': True
#                                     }
#             )
    def parse(self, response):
        # inspect_response(response, self)
        article_root = response.selector.xpath('//article')
        next_page = get_item(response.css('.next-page').xpath('./a/@data-page').extract())
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

        if len(next_page) != 0:
            self.para_dict["page"] = next_page
            next_url = self.root_urls + serialize(self.para_dict)
            yield scrapy.Request(next_url, callback=self.parse,dont_filter=True)





        # driver = webdriver.PhantomJS()  # (service_args = service_args)
        #
        # try:
        #     driver.set_page_load_timeout(20)
        #     driver.get(response.url)
        # except selenium.common.exceptions.TimeoutException:
        #     pass
        # #print(  self.driver.page_source)
        #
        # print(driver.page_source.find("python"))
        # filename = 'job' + '.html'
        # with open(filename, 'wb') as f:
        #     f.write(driver.page_source.encode('utf-8'))
        # inspect_response(response, self)
        # print(response.content.find("python"))
        # for selector in response.selector.xpath('//div/a'):
        #     pageIndex = selector.xpath("text()").extract()
        #     if( u'\u4e0b\u4e00\u9875' in pageIndex):
        #         url = response.urljoin(selector.xpath("@href").extract()[0])
        #         yield scrapy.Request(url, callback=self.parse)
        #
        # for href in response.selector.xpath('//li/a/@href').extract():
        #     url = response.urljoin(href)
        #     yield scrapy.Request(url, callback=self.parse_dir_contents)