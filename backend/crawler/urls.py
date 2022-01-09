from django.urls import path, include
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()    
router.register(r'url', UrlView, 'url')
router.register(r'site', SiteView, 'site')

urlpatterns = [
    path('api/', include(router.urls)),
]
