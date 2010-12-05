from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^(?P<id>[\d]+)\.html$', 'flickr.views.photo'),
    (r'^metro_score/(?P<score>[\d]+)\.html$', 'flickr.views.metro_score'),
    (r'^debug\.html', 'flickr.views.debug'),
    (r'^types\.html', 'flickr.views.types'),
    (r'^types/(?P<type>[\d]+)\.html$', 'flickr.views.type'),
    (r'^categories\.html', 'flickr.views.categories'),
    (r'^category/(?P<category>[\d]+)\.html$', 'flickr.views.category'),
    (r'^features/(?P<handle>.+)\.html', 'flickr.views.features'),
)
