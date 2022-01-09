from django.contrib import admin
from .models import Url, Site # add this
# Register your models here.

class UrlAdmin(admin.ModelAdmin):
    list_display = ('url',)

class SiteAdmin(admin.ModelAdmin):
    list_display = ('site',)

admin.site.register(Url, UrlAdmin) 
admin.site.register(Site, SiteAdmin) 
