from django.shortcuts import render
from rest_framework import viewsets
from .models import AtribuicaoChamado
from .serializers import AtribuicaoChamadoSerializer
from rest_framework.permissions import IsAdminUser

# Create your views here.
