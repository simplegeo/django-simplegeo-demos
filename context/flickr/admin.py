from django.contrib import admin
from context.flickr.models import Photo, Tag, Category, Type, Feature

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'longitude', 'latitude')

class TagAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

class TypeAdmin(admin.ModelAdmin):
    pass

class FeatureAdmin(admin.ModelAdmin):
    list_display = ('handle', 'name', 'type', 'category')

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Feature, FeatureAdmin)
