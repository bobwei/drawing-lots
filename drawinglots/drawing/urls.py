from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('drawinglots.drawing.views',
    url(r'^host/$', 'host', name='drawing_host'),
    url(r'^host/demo/(?P<game_id>[0-9]+)$', 'demo', name='drawing_demo'),
    url(r'^host/drawing/$', 'drawing', name='drawing_drawing'),
    url(r'^host/n_guests/$', 'n_guests', name='drawing_n_guests'),
    url(r'^guest/(?P<game_id>[0-9]+)$', 'guest', name='drawing_guest'),
)
