from django.urls import path, include
from rest_framework import routers
from .views import LocalViewSet

app_name = 'local'

router = routers.DefaultRouter()
router.register('', LocalViewSet, basename='locais')

urlpatterns = [
    path('', include(router.urls)),
]
