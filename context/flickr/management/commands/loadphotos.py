# Django imports
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

# Python imports
import httplib2
import optparse
import urllib
import simplejson as json
import time

class Command(BaseCommand):
    FLICKR_API = 'http://api.flickr.com/services/rest/'
    ARGS = {
        'panda_name': 'wang wang',
        'format': 'json',
        'extras': 'date_taken,owner_name,icon_server,geo,tags,views,media',
        'method': 'flickr.panda.getPhotos',
        'per_page': 100
    }

    args = ''
    help = "Load photos from Flickr's Wang Wang"
    option_list = BaseCommand.option_list + (
        optparse.make_option('--limit',
            action='store',
            dest='limit',
            default=False,
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
        if options['limit']:
            limit = int(options['limit'])
        else:
            limit = 100

        print "Loading about %s photos with API key %s ... " % (limit,
            settings.FLICKR_API_KEY)

        processed = 0
        while processed < limit:
            processed += self.get_photos()

        print "Loaded %s photos in all." % processed

    def get_photos(self):
        http = httplib2.Http()
        self.ARGS['api_key'] = settings.FLICKR_API_KEY
        url = '%s?%s' % (self.FLICKR_API, urllib.urlencode(self.ARGS))
        resp, content = http.request(url, "GET")
        if resp['status'] == '200':
            data = json.loads(content[14:-1])
            if data['stat'] != 'ok':
                return 0
            else:
                saved = 0
                for photo in data['photos']['photo']:
                    try:
                        self.save_photo(photo)
                        saved += 1
                    except:
                        pass

                if 'interval' in data['photos'] and \
                    data['photos']['interval'] > 0:
                    sleep = int(data['photos']['interval'])
                else:
                    sleep = 60

                print "Sleeping for %s seconds ..." % sleep
                time.sleep(sleep)

                return saved

    def save_photo(self, photo):
        print photo['id']
