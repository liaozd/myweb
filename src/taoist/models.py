from django.db import models


class VideoUrl(models.Model):
    request_url = models.URLField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    time_start_download = models.DateTimeField(blank=True, null=True)
    time_finish_download = models.DateTimeField(blank=True, null=True)
    time_start_upload = models.DateTimeField(blank=True, null=True)
    time_finish_upload = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return self.request_url
