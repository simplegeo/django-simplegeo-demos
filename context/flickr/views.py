# Django imports
from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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

    features_list = Feature.objects.filter(type=type).order_by('name')
    paginator = Paginator(features_list, 500)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        paginator_page = paginator.page(page)
    except (EmptyPage, InvalidPage):
        paginator_page = paginator.page(paginator.num_pages)

    return render_to_response('flickr/type.html', {
        'type': type,
        'paginator_page': paginator_page
    })

def categories(request):
    return render_to_response('flickr/categories.html', {
        'categories': Category.objects.all().order_by('name')
    })

def category(request, category):
    category = get_object_or_404(Category, pk=category)

    feature_list = Feature.objects.filter(category=category).order_by('name')
    paginator = Paginator(feature_list, 500)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        paginator_page = paginator.page(page)
    except (EmptyPage, InvalidPage):
        paginator_page = paginator.page(paginator.num_pages)

    return render_to_response('flickr/category.html', {
        'category': category,
        'paginator_page': paginator_page
    })

def features(request, handle):
    feature = get_object_or_404(Feature, pk=handle)

    # Cast QuerySet to a list right off the bat because sqlite implements COUNT(*) as full table scan.
    photo_list = list(Photo.objects.filter(features=feature)[:1000])
    paginator = Paginator(photo_list, 100)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        paginator_page = paginator.page(page)
    except (EmptyPage, InvalidPage):
        paginator_page = paginator.page(paginator.num_pages)

    return render_to_response('flickr/features.html', {
        'feature': feature,
        'paginator_page': paginator_page
    })


def debug(request):
    unknown = Category.objects.get(name='')
    features = Feature.objects.filter(category=unknown)

    return render_to_response('flickr/debug.html', {
        'features': features
    })
