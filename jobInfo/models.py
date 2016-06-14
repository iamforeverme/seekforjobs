from mongoengine import *


class JobInfo(Document):
    title = StringField(max_length=100, blank=True, default='')
    listing_date = DateTimeField(help_text='date published')
    location = StringField(max_length=100, blank=True, default='')
    sublocation = StringField(max_length=100, blank=True, default='')
    salary_range = StringField(max_length=100, blank=True, default='')
    url = StringField(max_length=100, blank=True, default='')

    meta = {"collection": "scrapy_items"}
