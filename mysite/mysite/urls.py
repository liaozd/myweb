from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
<<<<<<< HEAD

=======
    url(r'^$', 'myblog.views.index', name='index'),
>>>>>>> b76d8059e6a5a04b1e93194a31498be1c67ac792
    url(r'^admin/', include(admin.site.urls)),
)
