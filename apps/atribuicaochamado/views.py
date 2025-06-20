from django.shortcuts import render
from rest_framework import viewsets
from .models import AtribuicaoChamado
from .serializers import AtribuicaoChamadoSerializer
from rest_framework.permissions import IsAdminUser

# Create your views here.
class AtribuicaoChamadoViewSet(viewsets.ModelViewSet):
    queryset = AtribuicaoChamado.objects.all()
    serializer_class = AtribuicaoChamadoSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(atribuido_por=self.request.user)
