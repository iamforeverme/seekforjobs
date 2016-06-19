from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from jobInfo.models import JobInfo
from jobInfo.serializers import JobInfoSerializer
from celery import debug_task

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


# Create your views here.
@csrf_exempt
def page(request):
    """
    List all job information in database
    """
    if request.method == 'GET':
        jobs = JobInfo.objects()[3]
        key_word = "java"
        n_thread=5
        debug_task.delay(key_word, n_thread)
        serializer = JobInfoSerializer(jobs)
        return JSONResponse(serializer.data)