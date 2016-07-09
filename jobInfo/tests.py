from django.test import TestCase
from jobInfo.models import JobInfo
from mongoengine.connection import connect, disconnect,get_connection
from web import settings
from django.test import SimpleTestCase
from rest_framework.test import APIRequestFactory
import time,datetime
from views import AnalyzeJobCount,AnalyzeJobSalary

class JobInfoTestCase(SimpleTestCase):
    mongodb_name = 'testsuite'
    def setUp(self):
        disconnect()
        # try docker mongo
        host = settings._MONGODB_DATABASE_STR \
               % (settings._MONGODB_HOST, self.mongodb_name)
        connect(self.mongodb_name, host=host)
        self.__test_id=0

    def get_test_id(self):
        self.__test_id=self.__test_id+1
        return str(self.__test_id)

    def tearDown(self):
        connection = get_connection()
        connection.drop_database(self.mongodb_name)

    def test_job_information_can_be_fetched(self):
        JobInfo.objects.create(_id="101", title="software engineer", location="some where")
        """Animals that can speak are correctly identified"""
        job = JobInfo.objects.get(title="software engineer")
        self.assertEqual(job.location, 'some where')

    def test_analyze_job_count_verify_date(self):
        # Using the standard RequestFactory API to create a form POST request
        JobInfo.objects.create(_id=self.get_test_id(),
                               title="Front software engineer",
                               location="All Sydney",
                               listing_date=datetime.datetime(year=2016,month=6,day=15)
                               )
        JobInfo.objects.create(_id=self.get_test_id(),
                               title="Other front software engineer ",
                               location="All Sydney",
                               listing_date=datetime.datetime(year=2016, month=8, day=15)
                               )
        view = AnalyzeJobCount.as_view()
        factory = APIRequestFactory()
        request = factory.get(r'/jobInfo/analyze/count')
        response = view(request,start_time='2016-06-03',end_time='2016-07-04',key_word="front",location='sydney',format='json')
        response.render()
        expected_result='{"week":{"2016-06-13":1},"year":{"2016-01-01":1},"day":{"2016-06-14":1,"2016-06-15":0},"month":{"2016-06-01":1}}'
        self.assertEqual(expected_result, response.content)

    def test_analyze_job_count_verify_key_word(self):
        # Using the standard RequestFactory API to create a form POST request
        JobInfo.objects.create(_id=self.get_test_id(),
                               title="Front software engineer",
                               location="All Sydney",
                               listing_date=datetime.datetime(year=2016, month=6, day=15)
                               )
        JobInfo.objects.create(_id=self.get_test_id(),
                               title="Backend software engineer",
                               location="All Sydney",
                               listing_date=datetime.datetime(year=2016, month=6, day=17)
                               )
        view = AnalyzeJobCount.as_view()
        factory = APIRequestFactory()
        request = factory.get(r'/jobInfo/analyze/count')
        response = view(request, start_time='2016-06-03', end_time='2016-07-04', key_word="Front", location='sydney',
                        format='json')
        response.render()
        expected_result = '{"week":{"2016-06-13":1},"year":{"2016-01-01":1},"day":{"2016-06-14":1,"2016-06-15":0},"month":{"2016-06-01":1}}'
        self.assertEqual(expected_result, response.content)

    def test_analyze_job_count_verify_location(self):
        # Using the standard RequestFactory API to create a form POST request
        JobInfo.objects.create(_id=self.get_test_id(),
                               title="Front software engineer",
                               location="All Sydney",
                               listing_date=datetime.datetime(year=2016, month=6, day=15)
                               )
        JobInfo.objects.create(_id=self.get_test_id(),
                               title="Backend software engineer",
                               location="Merben",
                               listing_date=datetime.datetime(year=2016, month=6, day=17)
                               )
        view = AnalyzeJobCount.as_view()
        factory = APIRequestFactory()
        request = factory.get(r'/jobInfo/analyze/count')
        response = view(request, start_time='2016-06-03', end_time='2016-07-04', key_word="all", location='all',
                        format='json')
        response.render()
        expected_result = '{"week":{"2016-06-13":2},"year":{"2016-01-01":2},"day":{"2016-06-16":1,"2016-06-15":0},"month":{"2016-06-01":2}}'
        self.assertEqual(expected_result, response.content)

    def test_analyze_job_salary(self):
        JobInfo.objects.create(_id=self.get_test_id(),
                               title="Front software engineer",
                               location="All Sydney",
                               salary_index="750000",
                               listing_date=datetime.datetime(year=2016, month=6, day=15)
                               )

        JobInfo.objects.create(_id=self.get_test_id(),
                           title="Backend software engineer",
                           location="Merben",
                               salary_index="950000",
                           listing_date=datetime.datetime(year=2016, month=6, day=17)
                           )

        view = AnalyzeJobSalary.as_view()
        factory = APIRequestFactory()
        request = factory.get(r'/jobInfo/analyze/salary')
        response = view(request, start_time='2016-06-03', end_time='2016-07-04', key_word="all", location='all',
                        format='json')
        response.render()
        # the accurateness of the algorithm could be improved in the future
        expected_result = '[750000,950000]'
        self.assertEqual(expected_result, response.content)