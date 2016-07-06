from django.test import TestCase
from jobInfo.models import JobInfo
from mongoengine.connection import connect, disconnect,get_connection
from web import settings
from django.test import SimpleTestCase
from rest_framework.test import APIRequestFactory
import time,datetime
from views import AnalyzeJobCount

class JobInfoTestCase(SimpleTestCase):
    mongodb_name = 'testsuite'
    def setUp(self):
        disconnect()
        # try docker mongo
        host = settings._MONGODB_DATABASE_STR \
               % (settings._MONGODB_HOST, self.mongodb_name)
        connect(self.mongodb_name, host=host)

    def tearDown(self):
        connection = get_connection()
        connection.drop_database(self.mongodb_name)

    def test_job_information_can_be_fetched(self):
        JobInfo.objects.create(_id="101", title="software engineer", location="some where")
        """Animals that can speak are correctly identified"""
        job = JobInfo.objects.get(title="software engineer")
        self.assertEqual(job.location, 'some where')

    def test_analyze_job_count(self):
        # Using the standard RequestFactory API to create a form POST request
        JobInfo.objects.create(_id="101",
                               title="software engineer",
                               location="All Sydney",
                               listing_date=datetime.datetime(year=2016,month=6,day=15)
                               )
        view = AnalyzeJobCount.as_view()
        factory = APIRequestFactory()
        request = factory.get(r'/jobInfo/analyze/count/2016-06-03/2016-07-04/front/sydney')
        response = view(request)
        print(response)
