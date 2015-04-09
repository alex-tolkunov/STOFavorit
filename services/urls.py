__author__ = 'User'
from django.conf.urls import patterns, include, url
from services import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^service/(?P<service_id>\d+)/$', views.more, name='more'),
    url(r'^$', views.home)
)
