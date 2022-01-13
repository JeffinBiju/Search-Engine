from django.urls import path, include
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()    
router.register(r'query', QueryView, 'query')

urlpatterns = [
    path('api/', include(router.urls)),
]