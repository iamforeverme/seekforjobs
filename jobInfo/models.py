from django.db import models


class JobInfo(models.Model):
    onlineDate = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    location = models.CharField(max_length=100, blank=True, default='')
    workType = models.CharField(max_length=100, blank=True, default='')
    salary = models.CharField(max_length=100, blank=True, default='')
    tags = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ('onlineDate',)
