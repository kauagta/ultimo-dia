
from email.mime import image
from django.db import models

class usuario(models.Model):
    id_usuarios = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    senha = models.CharField(max_length=10)
    
