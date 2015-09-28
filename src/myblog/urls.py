from django.conf.urls import patterns, url
from myblog.views import BlogIndex, BlogDetail

urlpatterns = patterns('',
                       url(r'^$', BlogIndex.as_view(), name='index'),
                       url(r'^entry/(?P<slug>\S+)$', BlogDetail.as_view(), name='entry_detail'),
                       )

