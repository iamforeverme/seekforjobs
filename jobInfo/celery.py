from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from celery.utils.log import get_task_logger
from crawler.jobSpiders.crawler import run_spider

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web.settings')
app = Celery('web')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

logger = get_task_logger(__name__)

@app.task(name="debug_task")
def debug_task(key_word, n_crawls):
    logger.info("Call Page {0} : {1}".format(key_word,str(n_crawls)))
    # run_spider("software+engineer", 1, 1)


from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

import datetime

# @periodic_task(
#     run_every=datetime.timedelta(minutes=30),
#     name="task_scrapy_jobs_1",
#     ignore_result=True,
#     args=("program", 1),
# )
@app.task(name="task_scrapy_jobs")
def task_scrapy_jobs(key_word, crawl_num, n_crawls):
    """
    scrapy job informaiton
    """
    logger.info("Call Page {0} : {1} / {2}".format(key_word, str(crawl_num),str(n_crawls)))
    run_spider(key_word,crawl_num, n_crawls)
