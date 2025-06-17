from django.urls import path, include
from rest_framework import routers
from .views import ItemSolicitacaoViewSet

app_name = 'itemsolicitacao'

router = routers.DefaultRouter()
router.register('', ItemSolicitacaoViewSet, basename='itens')

urlpatterns = [
    path('', include(router.urls)),
]
