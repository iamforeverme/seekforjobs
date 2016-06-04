from django.test import TestCase
from jobInfo.models import JobInfo


class JobInfoTestCase(TestCase):
    def setUp(self):
        JobInfo.objects.create(title="software engineer", workType="full time")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        job = JobInfo.objects.get(title="software engineer")
        self.assertEqual(job.workType, 'full time')