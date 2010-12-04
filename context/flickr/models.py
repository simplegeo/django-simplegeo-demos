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

class Tag(models.Model):
    tag = models.CharField(max_length=100)
