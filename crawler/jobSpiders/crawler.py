from scrapy.crawler import Crawler
from jobSpiders.spiders.job_spider import JobSpider
from twisted.internet import reactor
from billiard import Process
import scrapy.signals as signals
from scrapy.utils.project import get_project_settings


class JobCrawlerScript(Process):
    def __init__(self, spider):
        Process.__init__(self)
        settings = get_project_settings()
        self.spider = spider
        self.crawler = Crawler(spider.__class__, settings)
        # self.crawler.configure()
        self.crawler.signals.connect(reactor.stop, signal=signals.spider_closed)

    def run(self):
        self.crawler.crawl(self.spider)
        # self.crawler.start()
        reactor.run()


def run_spider(key_word,crawl_num,n_crawls):
    spider = JobSpider(key_word,crawl_num,n_crawls)
    crawler = JobCrawlerScript(spider)
    crawler.start()
    crawler.join()