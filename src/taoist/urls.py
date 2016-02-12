from django.conf.urls import url

from taoist.views import TaoistView, TaoistSerialzerView
urlpatterns = [
    url(r'^$', TaoistView.as_view(), name='taoist'),
    url(r'^api/$', TaoistSerialzerView.as_view()),
]
