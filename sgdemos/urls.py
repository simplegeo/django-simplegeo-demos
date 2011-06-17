from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings


admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'website.views.index'),
    (r'^photos/', include('sgdemos.flickr.urls')),
    url(r'^places-google-maps/', 'django.views.generic.simple.direct_to_template', {'template': 'places-google-maps/index.html'}),
    (r'^(static|media)/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT})
)
