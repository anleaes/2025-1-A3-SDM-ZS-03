from django.urls import path, include
from rest_framework import routers
from .views import AvaliacaoViewSet

app_name = 'avaliacao'

router = routers.DefaultRouter()
router.register('', AvaliacaoViewSet, basename='avaliacoes')

urlpatterns = [
    path('', include(router.urls)),
]