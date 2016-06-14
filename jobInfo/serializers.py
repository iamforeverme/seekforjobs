from rest_framework import serializers
from jobInfo.models import JobInfo


class JobInfoSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    listing_date = serializers.DateTimeField()
    location = serializers.CharField(required=False, allow_blank=True, max_length=100)
    sublocation = serializers.CharField(required=False, allow_blank=True, max_length=100)
    salary_range = serializers.CharField(required=False, allow_blank=True, max_length=100)
    url = serializers.CharField(required=False, allow_blank=True, max_length=100)

    def restore_object(self, attrs, instance=None):
        if instance is not None:
            for k, v in attrs.iteritems():
                setattr(instance, k, v)
            return instance
        return JobInfo(**attrs)