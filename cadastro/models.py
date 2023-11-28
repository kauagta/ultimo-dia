from email.mime import image
from django.db import models



class Usuario(models.Model):   
    id_usuarios = models.CharField(max_length=140)
    email = models.EmailField(max_length=258)
    senha = models.CharField(max_length=140)
    email = models.EmailField(max_length=258)
    sobre_nome = models.CharField(max_length=258)
    telefone = models.CharField(max_length=170)
    confirme_senha = models.CharField(max_length=140)
    

    
        

