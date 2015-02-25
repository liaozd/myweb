from django.conf.urls import patterns, include, url
from django.contrib import admin
from myblog import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include('django_markdown.urls')),
    url(r'^', include('myblog.urls')),
    url(r'^entry/(?P<slug>\S+)$', views.BlogDetail.as_view(),)
)
