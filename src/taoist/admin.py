from django.contrib import admin
from .models import VideoUrl


class VideoUrlAdmin(admin.ModelAdmin):
    list_display = ['request_url', 'timestamp']

    class Meta:
        model = VideoUrl

admin.site.register(VideoUrl, VideoUrlAdmin)