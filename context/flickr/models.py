from django.db import models

class Photo(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    longitude = models.FloatField()
    latitude = models.FloatField()
    farm = models.PositiveIntegerField()
    secret = models.CharField(max_length=50)
    server = models.PositiveIntegerField()
    tags = models.ManyToManyField('Tag')
    features = models.ManyToManyField('Feature')
    metro_score = models.PositiveIntegerField()

    def __unicode__(self):
        return self.title

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
    type = models.ForeignKey('Type')
    category = models.ForeignKey('Category')

    def __unicode__(self):
        return self.name
