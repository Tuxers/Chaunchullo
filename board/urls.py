from django.conf.urls import patterns, url
from board import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<post_id>\d+)/$', views.get_post, name='get_post'),
    url(r'^post$', views.make_post, name='make_post'),
)
