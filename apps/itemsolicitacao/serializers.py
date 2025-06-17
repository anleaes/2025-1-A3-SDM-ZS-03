from rest_framework import serializers
from .models import ItemSolicitacao

class ItemSolicitacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemSolicitacao
        fields = '__all__'
