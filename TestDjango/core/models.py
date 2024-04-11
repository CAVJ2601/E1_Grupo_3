from django.db import models

# Create your models here.
class Usuario(models.Model):
    usuario = models.CharField(max_length=20, primary_key=True, verbose_name='Nombre usuario')
    nombre = models.CharField(max_length=50, verbose_name='Nombre completo')
    correo = models.CharField(max_length=50,verbose_name='Correo electronico')
    password = models.CharField(max_length=20,verbose_name='Password')
    fecha_nac = models.DateField(verbose_name='Fecha de nacimiento')
    direccion = models.CharField(max_length=100,verbose_name='Dirección despacho')

    def __str__(self):
        return self.usuario

