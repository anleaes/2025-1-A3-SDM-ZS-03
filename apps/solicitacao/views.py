from django.shortcuts import render
from rest_framework import viewsets
from .models import SolicitacaoTemporaria
from .serializers import SolicitacaoTemporariaSerializer

# Create your views here.
class SolicitacaoTemporariaViewSet(viewsets.ModelViewSet):
    queryset = SolicitacaoTemporaria.objects.all()
    serializer_class = SolicitacaoTemporariaSerializer
