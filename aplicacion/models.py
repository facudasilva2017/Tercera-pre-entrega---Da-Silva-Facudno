from django.db import models

# Create your models here.
class Consola(models.Model):
    nombre = models.CharField(max_length=50)
    compania = models.CharField(max_length=50)
    precio = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return f"{self.nombre}"
    
class Juego(models.Model):
    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    desarrolladora = models.CharField(max_length=50)
    precio = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return f"{self.nombre}"
 
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"