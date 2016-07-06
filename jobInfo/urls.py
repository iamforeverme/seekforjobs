from django.conf.urls import url, include
from . import views
from rest_framework import generics
from jobInfo.serializers import JobInfoSerializer
from jobInfo.models import JobInfo

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^job_list', generics.ListCreateAPIView.as_view(queryset=JobInfo.objects.all(),
                                                         serializer_class=JobInfoSerializer,
                                                         permission_classes=()),
                                                         name='job-list'),
    url(r'^init_data', views.init_data),
    url(r'^analyze/count/(?P<start_time>[\w\W]+)/(?P<end_time>[\w\W]+)/(?P<key_word>\w+)/(?P<location>\w+)',views.AnalyzeJobCount.as_view())

]