from rest_framework import serializers
from taoist.models import VideoUrl


class VideoUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoUrl
        fields = ('id', 'request_url',)
        # write_only_fields = ('id',)
