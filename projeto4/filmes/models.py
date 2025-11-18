from django.db import models

class Filme(models.Model):
    titulo = models.CharField(max_length=255)
    diretor = models.CharField(max_length=255)
    ano = models.PositiveIntegerField()
    genero = models.CharField(max_length=100)
    duracao = models.PositiveIntegerField()

def __str__(self):
    return self.nome