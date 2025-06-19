from django.urls import path, include
from rest_framework import routers
from .views import ChamadoManutencaoViewSet

app_name = 'chamadomanutencao'

router = routers.DefaultRouter()
router.register('', ChamadoManutencaoViewSet, basename='chamados')

urlpatterns = [
    path('', include(router.urls)),
]