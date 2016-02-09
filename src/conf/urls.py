from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include('django_markdown.urls')),
    url(r'^', include('myblog.urls')),
    url(r'^taoist/', include('taoist.urls'), name="taoist"),
]
