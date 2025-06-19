from django.urls import path, include
from rest_framework import routers
from .views import HistoricoAtividadeViewSet

app_name = 'historicoatividade'

router = routers.DefaultRouter()
router.register('', HistoricoAtividadeViewSet, basename='historico')

urlpatterns = [
    path('', include(router.urls)),
]