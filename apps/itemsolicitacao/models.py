from django.db import models
from django.db import models
from solicitacao.models import SolicitacaoTemporaria


# Create your models here.
class ItemSolicitacao(models.Model):
    solicitacao = models.ForeignKey(SolicitacaoTemporaria, on_delete=models.CASCADE, related_name='itens')
    descricao_problema = models.TextField('Descrição do problema')
    quantidade = models.PositiveIntegerField('Quantidade', default=1)

    class Meta:
        verbose_name = 'Item de Solicitação'
        verbose_name_plural = 'Itens de Solicitação'
        ordering = ['id']

    def __str__(self):
        return f"Item #{self.id} - Solicitação {self.solicitacao.id}"
