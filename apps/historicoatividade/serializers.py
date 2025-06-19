from rest_framework import serializers
from .models import HistoricoAtividade

class HistoricoAtividadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricoAtividade
        fields = '__all__'