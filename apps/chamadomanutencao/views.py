from django.shortcuts import render
from rest_framework import viewsets
from .models import ChamadoManutencao
from .serializers import ChamadoManutencaoSerializer
# Create your views here.
class ChamadoManutencaoViewSet(viewsets.ModelViewSet):
    queryset = ChamadoManutencao.objects.all()
    serializer_class = ChamadoManutencaoSerializer