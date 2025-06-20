from django.db import models
from django.db import models
from chamadomanutencao.models import ChamadoManutencao
from tecnico.models import Tecnico
from usuario.models import Usuario

# Create your models here.
class AtribuicaoChamado(models.Model):
    chamado = models.ForeignKey(ChamadoManutencao, on_delete=models.CASCADE, related_name='atribuicoes')
    tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE, related_name='atribuicoes')
    atribuido_por = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, related_name='atribuicoes_feitas')
    data_atribuicao = models.DateTimeField(auto_now_add=True)
    observacao = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Atribuição de Chamado'
        verbose_name_plural = 'Atribuições de Chamados'
        ordering = ['-data_atribuicao']

    def __str__(self):
        return f"{self.tecnico.usuario.first_name} atribuído ao chamado #{self.chamado.id}"
