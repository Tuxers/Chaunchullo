from django.conf.urls import patterns, url
from board import views

uuidRegex = ''

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<post_id>\d+)/$', views.get_post, name='get_post'),
    url(r'^post/$', views.make_post, name='make_post'),
    url(r'^file/(?P<file_name>[0-9a-fA-F]{8}[0-9a-fA-F]{4}[0-9a-f]{4}[0-9a-fA-F]{4}[0-9a-fA-F]{12}\.\w+)$', views.download_file, name='download_file')
)
