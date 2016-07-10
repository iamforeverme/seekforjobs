from mongoengine import *


class JobInfo(Document):
    _id = StringField(max_length=100, blank=False,primary_key=True)
    title = StringField(max_length=100, blank=True, default='')
    listing_date = DateTimeField(help_text='date published')
    location = StringField(max_length=100, blank=True, default='')
    sublocation = StringField(max_length=100, blank=True, default='')
    salary_range = StringField(max_length=100, blank=True, default='')
    salary_index = IntField()
    url = StringField(max_length=100, blank=True, default='')

    meta = {"collection": "scrapy_items"}
