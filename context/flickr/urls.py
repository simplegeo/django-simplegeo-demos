from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^(?P<id>[\d]+).html$', 'flickr.views.photo'),
)
