from django.conf.urls import url

from taoist.views import TaoistView

urlpatterns = [
    url(r'^$', TaoistView.as_view(), name='taoist'),
]
