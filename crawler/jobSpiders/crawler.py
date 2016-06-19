from scrapy.crawler import Crawler
from jobSpiders.spiders.job_spider import JobSpider
from twisted.internet import reactor
from billiard import Process
import scrapy.signals as signals
from scrapy.utils.project import get_project_settings


class JobCrawlerScript(Process):
    def __init__(self, spider,key_word,crawl_num,n_crawls):
        Process.__init__(self)
        settings = get_project_settings()
        self.spider = spider
        self.crawler = Crawler(spider.__class__, settings)
        # self.crawler.configure()
        self.crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
        self.n_crawls = n_crawls
        self.crawl_num = crawl_num
        self.key_word = key_word

    def run(self):
        self.crawler.crawl(self.spider,key_word=self.key_word,crawl_num=self.crawl_num,n_crawls=self.n_crawls)
        reactor.run()


def run_spider(key_word,crawl_num,n_crawls):
    spider = JobSpider(key_word=key_word,crawl_num=crawl_num,n_crawls=n_crawls)
    crawler = JobCrawlerScript(spider,key_word=key_word,crawl_num=crawl_num,n_crawls=n_crawls)
    crawler.start()
    crawler.join()