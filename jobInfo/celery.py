from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from celery.utils.log import get_task_logger

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web.settings')
app = Celery('web')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

logger = get_task_logger(__name__)

@app.task(name="debug_task")
def debug_task():
    logger.info("Sent feedback email")


from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger


@periodic_task(
    run_every=(crontab(minute='*/1')),
    name="task_save_latest_flickr_image",
    ignore_result=True
)
def task_save_latest_flickr_image():
    """
    Saves latest image from Flickr
    """
    print("hello world")
    logger.info("Saved image from Flickr")