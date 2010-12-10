# Django imports
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

# Python imports
import httplib2
import optparse
import urllib
import simplejson as json
import time
from simplegeo.context import ContextClient

# Project imports
from context.flickr.models import Photo, Tag, Category, Type, Feature

class Command(BaseCommand):
    FLICKR_API = 'http://api.flickr.com/services/rest/'
    ARGS = {
        'panda_name': 'wang wang',
        'format': 'json',
        'extras': 'date_taken,owner_name,icon_server,geo,tags,views,media',
        'method': 'flickr.panda.getPhotos',
        'per_page': 100,
        'nojsoncallback': 1
    }

    args = ''
    help = "Load photos from Flickr's Wang Wang"
    option_list = BaseCommand.option_list + (
        optparse.make_option('--limit',
            action='store',
            dest='limit',
            default=500,
            help='Number of photos to load'),
        )

    def handle(self, *args, **options):
        """
{
    "photos": {
        "total": 117, 
        "photo": [
            {
                "date_taken": "2010-01-26 06:49:29", 
                "title": "self", 
                "farm": 5, 
                "media": "photo", 
                "views": "88", 
                "tags": "portrait selfportrait", 
                "longitude": -2.427978, 
                "server": "4030", 
                "latitude": 53.581294999999997, 
                "secret": "4c6b84488b", 
                "ownername": "Lily-Wren", 
                "owner": "40354622@N05", 
                "id": "4306098032", 
                "accuracy": "11"
            }, 
            {
                "date_taken": "2010-11-26 20:26:43", 
                "title": "The Word Alive", 
                "farm": 6, 
                "media": "photo", 
                "views": "0", 
                "tags": "word photography alive underoath the", 
                "longitude": -82.44323, 
                "server": "5285", 
                "latitude": 27.960291000000002, 
                "secret": "3cb037a28a", 
                "ownername": "Rocket City Photography", 
                "owner": "54153623@N06", 
                "id": "5227637930", 
                "accuracy": "15"
            }
        ], 
        "interval": 60, 
        "panda": "wang wang", 
        "lastupdate": 1291485820
    }, 
    "stat": "ok"
}
"""
        self.context = ContextClient(settings.SIMPLEGEO_KEY,
            settings.SIMPLEGEO_SECRET)

        print "Loading about %s photos with API key %s ... " % (
            options['limit'], settings.FLICKR_API_KEY)

        processed = 0
        while processed < options['limit']:
            try:
                processed += self.get_photos()
            except Exception, e:
                "ERROR: %s" % str(e)

        print "Loaded %s photos in all." % processed

    def get_photos(self):
        http = httplib2.Http(timeout=3)
        self.ARGS['api_key'] = settings.FLICKR_API_KEY
        url = '%s?%s' % (self.FLICKR_API, urllib.urlencode(self.ARGS))

        resp, content = http.request(url, "GET")
        if resp['status'] == '200':
            data = json.loads(content)
            if data['stat'] != 'ok':
                return 0
            else:
                print "Running %s photos through SimpleGeo Context ..." % len(data['photos']['photo'])
                saved = 0
                for photo in data['photos']['photo']:
                    try:
                        self.save_photo(photo)
                        saved += 1
                    except Exception, e:
                        print "ERROR: %s" % str(e)

                return saved

    def save_photo(self, photo):
        try:
            photo = Photo.objects.get(id=photo['id'])
            return
        except:
            pass

        context = self.context.get_context(photo['latitude'],
            photo['longitude'])

        tags = []
        for tag in photo['tags'].split(' '):
            try:
                t = Tag.objects.get(tag=tag)
            except Tag.DoesNotExist:
                t = Tag()
                t.tag = tag
                t.save()

            tags.append(t)

        p = Photo()
        p.id = photo['id']
        p.owner = photo['owner']
        p.title = photo['title']
        p.latitude = photo['latitude']
        p.longitude = photo['longitude']
        p.farm = photo['farm']
        p.secret = photo['secret']
        p.server = photo['server']

        try:
            p.metro_score = int(context['demographics']['metro_score'])
        except:
            p.metro_score = 0

        p.save()
        p.tags = tags

        print p.id
        features = []
        for feature in context['features']:
            try:
                category = Category.objects.get(name=feature['classifiers'][0]['category'])
            except Category.DoesNotExist:
                category = Category()
                category.name = feature['classifiers'][0]['category']
                category.save()

            try:
                type = Type.objects.get(name=feature['classifiers'][0]['type'])
            except Type.DoesNotExist:
                type = Type()
                type.name = feature['classifiers'][0]['type']
                type.save()

            try:
                f = Feature.objects.get(handle=feature['handle'])
            except Feature.DoesNotExist:
                f = Feature()
                f.handle = feature['handle']
                f.name = feature['name']
                f.type = type
                f.category = category 
                f.save()

            print "+-> %s (%s, %s)" % (f.name, f.category, f.type)

            features.append(f)

        p.features = features
