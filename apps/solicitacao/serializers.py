from rest_framework import serializers
from .models import SolicitacaoTemporaria

class SolicitacaoTemporariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitacaoTemporaria
        fields = '__all__'