from django.db import models

# Create your models here.
#Modelo de categoría
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name= 'Id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name= 'Nombre de la categoría')

    def __str__(self):
        return self.nombreCategoria
#modelo de vehiculo
class Vehiculo(models.Model):
    patente = models.CharField(max_length=6, primary_key=True, verbose_name='Patente')
    marca = models.CharField(max_length=20, verbose_name='Marca de Vehículo')
    modelo = models.CharField(max_length=20, null=True, blank=True, verbose_name='Modelo')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='vehiculos/', verbose_name='Imagen del vehículo')

    def __str__(self):
        return self.patente
