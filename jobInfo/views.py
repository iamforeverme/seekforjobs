from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from jobInfo.models import JobInfo
from jobInfo.serializers import JobInfoSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from celery import task_scrapy_jobs
from django.shortcuts import render
from rest_framework.views import APIView
import time,datetime

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


# Create your views here.
@api_view(['POST'])
@csrf_exempt
def init_data(request):
    """
    List all job information in database
    """
    if request.method == 'POST':
        data = request.data
        key_word=data["key_word"]
        n_threads = 1
        for thread in range(1, n_threads + 1):
            task_scrapy_jobs.delay(key_word, thread, n_threads)
        return Response(data={"key_word":key_word},status=status.HTTP_200_OK)


def index(request):
    return render(request, 'jobInfo/index.html', None)


class AnalyzeJobCount(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    def get(self, request, start_time,end_time,key_word,location,format=None):
        """
        Return a list of all users.
        http://127.0.0.1:8000/jobInfo/analyze/count/2013-11-12/2014-12-5/software/sydney
        """
        start_time_date_time=time.mktime(time.strptime(start_time,"%Y-%m-%d"))
        end_time_date_time = time.mktime(time.strptime(end_time, "%Y-%m-%d"))
        tdelta=datetime.timedelta(seconds=end_time_date_time-start_time_date_time).days

        return Response(tdelta)