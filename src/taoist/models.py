from django.db import models

import sys
print(sys.path)


class VideoUrl(models.Model):
    request_url = models.URLField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return self.request_url
