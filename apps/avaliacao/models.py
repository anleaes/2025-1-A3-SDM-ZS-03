from django.db import models
from django.db import models
from chamadomanutencao.models import ChamadoManutencao

# Create your models here.
class Avaliacao(models.Model):
    chamado = models.OneToOneField(ChamadoManutencao, on_delete=models.CASCADE, related_name='avaliacao')
    nota = models.IntegerField('Nota de satisfação', choices=[(1, '1 estrela'), (2, '2 estrelas'), (3, '3 estrelas'), (4, '4 estrelas'), (5, '5 estrelas')])
    comentario = models.TextField('Comentário', blank=True, null=True)
    data_avaliacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        ordering = ['-data_avaliacao']

    def __str__(self):
        return f"Avaliação #{self.id} - Chamado #{self.chamado.id}"
