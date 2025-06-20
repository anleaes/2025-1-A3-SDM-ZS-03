from django.urls import path, include
from rest_framework import routers
from .views import TecnicoViewSet

app_name = 'tecnico'

router = routers.DefaultRouter()
router.register('', TecnicoViewSet, basename='tecnicos')

urlpatterns = [
    path('', include(router.urls)),
]