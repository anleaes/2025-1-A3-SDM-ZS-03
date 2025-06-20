from django.urls import path, include
from rest_framework import routers
from .views import AtribuicaoChamadoViewSet

app_name = 'atribuicao'

router = routers.DefaultRouter()
router.register('', AtribuicaoChamadoViewSet, basename='atribuicoes')

urlpatterns = [
    path('', include(router.urls)),
]
