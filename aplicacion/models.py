from django.db import models

# Create your models here.

class Artista(models.Model):
    nombre=models.CharField(max_length=50, primary_key=True)
    pais=models.CharField(max_length=25, null=False)