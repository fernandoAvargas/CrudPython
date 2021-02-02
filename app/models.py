from django.db import models

# Create your models here.
class Cars(models.Model):
    indice = models.IntegerField()
    Modelo = models.CharField(max_length=180)
    Marca = models.CharField(max_length=150)
    Ano = models.IntegerField()
    Inclusao = models.DateTimeField()
    Placa = models.CharField(max_length=30)
    Chassi = models.CharField(max_length=100)
    CLRV = models.CharField(max_length=100)
