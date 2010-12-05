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
   
def types(request):
    return render_to_response('flickr/types.html', {
        'types': Type.objects.all().order_by('name')
    })

def type(request, type):
    type = get_object_or_404(Type, pk=type)
    return render_to_response('flickr/type.html', {
        'type': type,
        'features': Feature.objects.filter(type=type).order_by('name')
    })

def categories(request):
    return render_to_response('flickr/categories.html', {
        'categories': Category.objects.all().order_by('name')
    })

def category(request, category):
    category = get_object_or_404(Category, pk=category)
    return render_to_response('flickr/category.html', {
        'category': category,
        'features': Feature.objects.filter(category=category).order_by('name')
    })

def features(request, handle):
    feature = get_object_or_404(Feature, pk=handle)
    return render_to_response('flickr/results.html', {
        'feature': feature,
        'photos': Photo.objects.filter(features=feature)
    })
   

def debug(request):
    unknown = Category.objects.get(name='')
    features = Feature.objects.filter(category=unknown)

    return render_to_response('flickr/debug.html', {
        'features': features
    })
