from django.db import models
from django.db import models
from usuario.models import Usuario

# Create your models here.
class Tecnico(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='perfil_tecnico')
    especialidade = models.CharField(max_length=100)
    registro_profissional = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = 'Técnico'
        verbose_name_plural = 'Técnicos'
        ordering = ['usuario__first_name']

    def __str__(self):
        return f"{self.usuario.first_name} ({self.especialidade})"
