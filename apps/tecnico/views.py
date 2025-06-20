from django.shortcuts import render
from rest_framework import viewsets
from .models import Tecnico
from .serializers import TecnicoSerializer

# Create your views here.
class TecnicoViewSet(viewsets.ModelViewSet):
    queryset = Tecnico.objects.all()
    serializer_class = TecnicoSerializer