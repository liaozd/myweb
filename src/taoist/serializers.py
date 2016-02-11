from rest_framework import serializers
from taoist.models import VideoUrl


class VideoUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoUrl
        fields = ('request_url',)

