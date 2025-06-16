from django.urls import path, include
from rest_framework import routers
from .views import SolicitacaoTemporariaViewSet

app_name = 'solicitacao'

router = routers.DefaultRouter()
router.register('', SolicitacaoTemporariaViewSet, basename='solicitacoes')

urlpatterns = [
    path('', include(router.urls)),
]
