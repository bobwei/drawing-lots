from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic.simple import redirect_to
from django.core.urlresolvers import reverse_lazy

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    (r'^$', redirect_to, {'url': reverse_lazy('drawing_host')}),
    url(r'^drawing/', include('drawinglots.drawing.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'auth/login.html'}),
    url(r'accounts', include('social_auth.urls')),
)

urlpatterns += patterns('',  
(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),)
