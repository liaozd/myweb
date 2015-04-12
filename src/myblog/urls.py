from django.conf.urls import patterns, url
from .import views

urlpatterns = patterns('',
                       url(r'^$', views.BlogIndex.as_view(), name='index'),
                       url(r'^entry/(?P<slug>\S+)$', views.BlogDetail.as_view(), name='entry_detail'),
                       )

