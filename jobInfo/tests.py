from django.test import TestCase
from jobInfo.models import JobInfo
from mongoengine.connection import connect, disconnect,get_connection
from web import settings
from django.test import SimpleTestCase


class JobInfoTestCase(SimpleTestCase):
    mongodb_name = 'testsuite'
    def setUp(self):
        disconnect()
        try:
            # try docker mongo
            host = settings._MONGODB_DATABASE_STR \
                   % (settings._MONGODB_HOST, self.mongodb_name)
            connect(self.mongodb_name, host=host)
        except Exception as e:
            # if fail, turn to localhost
            host = settings._MONGODB_DATABASE_STR \
                   % ("localhost", self.mongodb_name)
            connect(self.mongodb_name, host=host)

    def tearDown(self):
        connection = get_connection()
        connection.drop_database(self.mongodb_name)

    def test_job_information_can_be_fetched(self):
        JobInfo.objects.create(_id="101", title="software engineer", location="some where")
        """Animals that can speak are correctly identified"""
        job = JobInfo.objects.get(title="software engineer")
        self.assertEqual(job.location, 'some where')