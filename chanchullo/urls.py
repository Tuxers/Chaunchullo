from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chanchullo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include('board.urls')),
    url(r'^board/', include('board.urls', namespace='board')),
    url(r'^admin/', include(admin.site.urls)),
)
