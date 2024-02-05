from django.contrib import admin
from .models import GalleryMediaFile, Visitor, UniqueVisitorCount
# Register your models here.

admin.site.register(GalleryMediaFile)
admin.site.register(Visitor)
admin.site.register(UniqueVisitorCount)
