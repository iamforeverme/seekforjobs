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