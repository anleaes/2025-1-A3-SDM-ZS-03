from django.shortcuts import render
from rest_framework import viewsets
from .models import ItemSolicitacao
from .serializers import ItemSolicitacaoSerializer

# Create your views here.
class ItemSolicitacaoViewSet(viewsets.ModelViewSet):
    queryset = ItemSolicitacao.objects.all()
    serializer_class = ItemSolicitacaoSerializer
