from rest_framework import serializers
from jobInfo.models import JobInfo


class JobInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobInfo
        fields = ('id', 'onlineDate', 'title', 'location', 'workType', 'salary','tags')