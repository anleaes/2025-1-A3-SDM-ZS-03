from rest_framework import serializers
from .models import ChamadoManutencao

class ChamadoManutencaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChamadoManutencao
        fields = '__all__'
