from django.db import models

# Create your models here.
from django.db import models

class Usuario(models.Model):
    first_name = models.CharField('Primeiro Nome', max_length=50)
    last_name = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('E-mail', null=False, blank=False)
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    )
    gender = models.CharField('Gênero', max_length=1, choices=GENDER_CHOICES)
    address = models.CharField('Endereço', max_length=255)
    phone = models.CharField('Telefone', max_length=15)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['id']
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"