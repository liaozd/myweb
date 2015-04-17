from django.conf.urls import patterns, include, url
from django.contrib import admin
from mysite import settings

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^markdown/', include('django_markdown.urls')),
                       url(r'^', include('myblog.urls')),
                       )
