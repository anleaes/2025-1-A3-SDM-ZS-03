from rest_framework import serializers
from .models import AtribuicaoChamado
from tecnico.serializers import TecnicoSerializer
from usuario.serializers import UsuarioSerializer
from chamadomanutencao.serializers import ChamadoManutencaoSerializer

class AtribuicaoChamadoSerializer(serializers.ModelSerializer):
    tecnico = TecnicoSerializer(read_only=True)
    chamado = ChamadoManutencaoSerializer(read_only=True)
    atribuido_por = UsuarioSerializer(read_only=True)

    class Meta:
        model = AtribuicaoChamado
        fields = '__all__'
