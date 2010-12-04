# Django imports
from django.shortcuts import render_to_response, get_object_or_404

# Project imports
from context.flickr.models import Photo, Tag, Category, Type, Feature


def photo(request, id):
    return render_to_response('flickr/photo.html', {
        'photo': get_object_or_404(Photo, id=id)
    })


def metro_score(request, score):
    return render_to_response('flickr/results.html', {
        'photos': Photo.objects.filter(metro_score=score)
    })
   

def debug(request):
    unknown = Category.objects.get(name='')
    features = Feature.objects.filter(category=unknown)

    return render_to_response('flickr/debug.html', {
        'features': features
    })
