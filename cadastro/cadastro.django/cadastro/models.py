from django.db import models

class usuario(models.Model):
    nome = models.CharField(max_length=10)
    email = models.EmailField(max_length=250)
    senha = models.CharField(max_length=10)
    