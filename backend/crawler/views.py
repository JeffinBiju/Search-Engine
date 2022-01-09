from django.shortcuts import render
from rest_framework import viewsets 
from .serializers import UrlSerializer, SiteSerializer
from .models import Url, Site
from rest_framework.response import Response
from bs4 import BeautifulSoup
import requests
import re

# Create your views here.

class UrlView(viewsets.ModelViewSet):
    
    queryset = Url.objects.all()
    serializer_class = UrlSerializer


class SiteView(viewsets.ModelViewSet):
    serializer_class = SiteSerializer
    queryset = Site.objects.all() 

    def create(self, request):

        url = Url(url=request.data['site'])
        url.save()
        req = requests.get(request.data['site'])
        soup = BeautifulSoup(req.content, 'html.parser')
        for link in soup.find_all('a', attrs={'href': re.compile("^http://")}):
            print(link.get('href'))
            url = Url(url=link.get('href'))
            url.save()
        return Response({'data':'data'})
    