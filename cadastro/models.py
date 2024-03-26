from django.db import models

# Create your models here.

class Cadastro(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    senha = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.nome}: {self.data} - {self.email}'
    class Meta:
        verbose_name = 'Formulário de cadastro'
        verbose_name_plural = 'Formulário de cadastros'
        ordering = ['-data']