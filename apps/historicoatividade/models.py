from django.db import models
from django.db import models
from chamadomanutencao.models import ChamadoManutencao
from usuario.models import Usuario

# Create your models here.
class HistoricoAtividade(models.Model):
    chamado = models.ForeignKey(ChamadoManutencao, on_delete=models.CASCADE, related_name='historico')
    autor = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, related_name='atividades')
    descricao = models.TextField('Descrição da atividade')
    data_hora = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Histórico de Atividade'
        verbose_name_plural = 'Históricos de Atividade'
        ordering = ['-data_hora']

    def __str__(self):
        return f"{self.data_hora.strftime('%d/%m %H:%M')} - Chamado #{self.chamado.id}"