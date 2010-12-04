from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^(?P<id>[\d]+).html$', 'flickr.views.photo'),
    (r'^metro_score/(?P<score>[\d]+).html$', 'flickr.views.metro_score'),
    (r'^debug.html', 'flickr.views.debug'),
)
