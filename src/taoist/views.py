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
        videourls = VideoUrl.objects.all()
        serializer = VideoUrlSerializer(videourls, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = VideoUrlSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
