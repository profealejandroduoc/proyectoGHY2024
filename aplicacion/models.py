from django.db import models

# Create your models here.

class Artista(models.Model):
   
    nombre=models.CharField(max_length=50,null=False, primary_key=True)