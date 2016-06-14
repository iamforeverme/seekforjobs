from django.conf.urls import url, include
from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^page', views.page),
    url(r'^job_list', views.JobList.as_view(), name='job-list'),
]