from rest_framework import serializers
from .models import Url, Site

class UrlSerializer(serializers.ModelSerializer):
      class Meta:
        model = Url
        fields = ('id', 'url')
      
class SiteSerializer(serializers.ModelSerializer):
      class Meta:
        model = Site
        fields = ('id', 'site')
        

