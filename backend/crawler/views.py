from django.shortcuts import render
from rest_framework import viewsets 
from .serializers import UrlSerializer, SiteSerializer
from .models import Url, Site
from rest_framework.response import Response
from bs4 import BeautifulSoup
import requests
from rest_framework.decorators import action
import re

# Create your views here.

class UrlView(viewsets.ModelViewSet):
    
    queryset = Url.objects.all()
    serializer_class = UrlSerializer

    @action(detail=False)
    def crawl(self, request):
        queryset = Url.objects.all()
        for query in queryset.iterator():
            url = query.url
            try:
                response = requests.get(url)
            except:
                continue
            soup = BeautifulSoup(response.content, 'html.parser')
            for link in soup.find_all('a', href=True):
                link = link.get('href')
                if link[-1] == '/':
                    link = link[:-1]
                if re.match('https.*', link):
                    urlobj = Url(url=link)
                    try:
                        urlobj.save()
                    except:
                        continue
                else:
                    urlobj = Url(url=url+link)
                    try:
                        urlobj.save()
                    except:
                        continue
        return Response({'data':'data'})


class SiteView(viewsets.ModelViewSet):
    serializer_class = SiteSerializer
    queryset = Site.objects.all() 

    def create(self, request):
        url = Url(url=request.data['site'])
        url.save()
        response = requests.get(request.data['site'])
        soup = BeautifulSoup(response.content, 'html.parser')
        for loc in soup.find_all('loc'):
            link = loc.string
            if link[-1] == '/':
                link = link[:-1]
            urlobj = Url(url=link)
            try:
                urlobj.save()
            except:
                continue
        return Response({'data':'data'})
    