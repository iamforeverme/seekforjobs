from rest_framework_mongoengine.serializers import DocumentSerializer
from jobInfo.models import JobInfo


class JobInfoSerializer(DocumentSerializer):
    class Meta:
        model = JobInfo
        depth = 2
        # related_model_validations = {'owner': User, 'post': Post}
        # exclude = ('isApproved',)