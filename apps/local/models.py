from django.db import models

# Create your models here.
class Local(models.Model):
    nome = models.CharField('Nome do Local', max_length=100)
    bloco = models.CharField('Bloco', max_length=50, blank=True, null=True)
    andar = models.CharField('Andar', max_length=20, blank=True, null=True)
    sala = models.CharField('Sala', max_length=50, blank=True, null=True)
    referencia = models.TextField('Referência/Observações', blank=True, null=True)
