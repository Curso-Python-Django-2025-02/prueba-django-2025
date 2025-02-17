from django.db import models

# Create your models here.
class Perfil(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    preferencias = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.nombre} {self.apellidos}'