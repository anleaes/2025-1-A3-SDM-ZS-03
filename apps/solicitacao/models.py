from django.db import models

# Create your models here.
from django.db import models
from usuario.models import Usuario

class SolicitacaoTemporaria(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='solicitacoes')
    data_criacao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30, default='Em aberto')

    class Meta:
        verbose_name = 'Solicitação Temporária'
        verbose_name_plural = 'Solicitações Temporárias'
        ordering = ['-data_criacao']

    def __str__(self):
        return f"Solicitação #{self.id} - {self.usuario.first_name}"
