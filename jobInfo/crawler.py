from scrapy.crawler import Crawler
from scrapy.conf import settings
from .crawler.jobSpiders.jobSpiders.spiders.job_spider import JobSpider
from scrapy import log, project
from twisted.internet import reactor
from billiard import Process
import scrapy.signals as signals
from scrapy.utils.project import get_project_settings


class JobCrawlerScript(Process):
        def __init__(self, spider):
            Process.__init__(self)
            settings = get_project_settings()
            self.crawler = Crawler(settings)
            self.crawler.configure()
            self.crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
            self.spider = spider

        def run(self):
            self.crawler.crawl(self.spider)
            self.crawler.start()
            reactor.run()


def run_spider(url):
    spider = JobSpider()
    crawler = JobCrawlerScript(spider)
    crawler.start()
    crawler.join()