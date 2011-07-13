from django.db import models

# From http://www.flickr.com/services/api/flickr.photos.licenses.getInfo.html
LICENSES = {
    '0': {
        'text': 'All Rights Reserved',
        'url': 'http://en.wikipedia.org/wiki/All_rights_reserved'
        },
    '1': {
        'text': 'Attribution-NonCommercial-ShareAlike License',
        'url': 'http://creativecommons.org/licenses/by-nc-sa/2.0/'
        },
    '2': {
        'text': 'Attribution-NonCommercial License',
        'url': 'http://creativecommons.org/licenses/by-nc/2.0/'
        },
    '3': {
        'text': 'Attribution-NonCommercial-NoDerivs License',
        'url': 'http://creativecommons.org/licenses/by-nc-nd/2.0/'
        },
    '4': {
        'text': 'Attribution License',
        'url': 'http://creativecommons.org/licenses/by/2.0/'
        },
    '5': {
        'text': 'Attribution-ShareAlike License',
        'url': 'http://creativecommons.org/licenses/by-sa/2.0/'
        },
    '6': {
        'text': 'Attribution-NoDerivs License',
        'url': 'http://en.wikipedia.org/wiki/All_rights_reserved'
        },
    '7': {
        'text': 'No known copyright restrictions',
        'url': 'http://flickr.com/commons/usage/'
        },
    }

class Photo(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    longitude = models.FloatField()
    latitude = models.FloatField()
    owner = models.CharField(max_length=200)
    farm = models.PositiveIntegerField()
    license = models.CharField(max_length=1)
    secret = models.CharField(max_length=50)
    server = models.PositiveIntegerField()
    tags = models.ManyToManyField('Tag')
    features = models.ManyToManyField('Feature')
    metro_score = models.PositiveIntegerField()

    def __unicode__(self):
        if self.title:
            return self.title
        else:
            return str(self.id)

    @property
    def srcurl(self):
        return "http://farm%s.static.flickr.com/%s/%s_%s_z.jpg" % (self.farm,
            self.server, self.id, self.secret)

    @property
    def license_text(self):
        return LICENSES[self.license]['text']

    @property
    def license_url(self):
        return LICENSES[self.license]['url']

class Tag(models.Model):
    tag = models.CharField(max_length=100, db_index=True)

    def __unicode__(self):
        return self.tag


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __unicode__(self):
        if self.name:
            return self.name
        else:
            return "No Category"


class Type(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __unicode__(self):
        return self.name


class Feature(models.Model):
    handle = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=255)
    type = models.ForeignKey('Type', related_name='features')
    category = models.ForeignKey('Category')

    def __unicode__(self):
        return self.name
