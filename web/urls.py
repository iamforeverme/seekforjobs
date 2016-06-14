from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets




# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^jobInfo/', include('jobInfo.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
