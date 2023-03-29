from django.db import models

# Create your models here.

class nota(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    data = models.DateTimeField('data da nota')

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)