from django.shortcuts import render
from rest_framework import viewsets
from .models import Local
from .serializers import LocalSerializer

# Create your views here.
class LocalViewSet(viewsets.ModelViewSet):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer
