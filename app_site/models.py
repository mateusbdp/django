from django.db import models

# Create your models here.
from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=15, null=True, blank=True)
    endereco = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
