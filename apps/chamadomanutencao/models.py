from django.db import models
from django.db import models
from solicitacao.models import SolicitacaoTemporaria
from usuario.models import Usuario  
#from local.models import Local  

# Create your models here.
class ChamadoManutencao(models.Model):
    solicitacao = models.OneToOneField(SolicitacaoTemporaria, on_delete=models.CASCADE, related_name='chamado')
    data_abertura = models.DateTimeField(auto_now_add=True)
    data_conclusao = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=30, default='Aberto')
    prioridade = models.CharField(max_length=20, choices=[
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta')
    ])
    tecnicos = models.ManyToManyField(Usuario, related_name='chamados')  # assume que Usuario com tipo='Técnico'
    #local = models.ForeignKey('local.Local', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Chamado de Manutenção'
        verbose_name_plural = 'Chamados de Manutenção'
        ordering = ['-data_abertura']

    def __str__(self):
        return f"Chamado #{self.id} - {self.status}"