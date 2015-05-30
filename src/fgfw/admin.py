from django.contrib import admin
from src.fgfw.models import YouTubeURL


class YouTubeURLAdmin(admin.ModelAdmin):
    list_display = ['request_url', 'timestamp']

    class Meta:
        model = YouTubeURL

admin.site.register(YouTubeURL, YouTubeURLAdmin)