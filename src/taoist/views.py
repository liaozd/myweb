from django.views.generic import CreateView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from taoist.models import VideoUrl
from taoist.forms import VideoUrlForm
from taoist.serializers import VideoUrlSerializer


class TaoistView(CreateView):
    model = VideoUrl
    form_class = VideoUrlForm
    template_name = 'taoist.html'
    success_url = '/taoist/'


class TaoistSerialzerView(APIView):
    def get(self, request, format=None):
        all_urls = VideoUrl.objects.all()
        serializer = VideoUrlSerializer(all_urls, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        videourl_id = request.data.get('id')
        if videourl_id:
            videourl_object = VideoUrl.objects.get(id=videourl_id)
            serializer = VideoUrlSerializer(videourl_object, data=request.data, partial=True)
        else:
            serializer = VideoUrlSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
