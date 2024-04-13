from django.db import models

# Create your models here.
class Region(models.Model):
    id_region = models.CharField(max_length=3, primary_key=True, verbose_name='Id region')
    nombre_region = models.CharField(max_length=50, verbose_name='Nombre region')

    def __str__(self):
        return self.nombre_region

class Comuna(models.Model):
    id_comuna = models.CharField(max_length=5, primary_key=True, verbose_name='Id comuna')
    nombre_comuna = models.CharField(max_length=50, verbose_name='Nombre comuna')
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_comuna

class Usuario(models.Model):
    usuario = models.CharField(max_length=20, primary_key=True, verbose_name='Nombre usuario')
    nombre = models.CharField(max_length=50, verbose_name='Nombre completo')
    correo = models.CharField(max_length=50,verbose_name='Correo electronico')
    password = models.CharField(max_length=20,verbose_name='Password')
    fecha_nac = models.DateField(verbose_name='Fecha de nacimiento')
    direccion = models.CharField(max_length=100,verbose_name='Dirección despacho')
    comuna = models.ForeignKey(Comuna,on_delete=models.CASCADE)
    region = models.ForeignKey(Region,on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario
    
class CategoriaJuego(models.Model):
    id_categoria = models.CharField(max_length=20, primary_key=True, verbose_name='Código categoría')
    nombre_categoria = models.CharField(max_length=50, verbose_name='Nombre categoría')

    def __str__(self):
        return self.nombre_categoria
    
class Juego(models.Model):
    id_juego = models.CharField(max_length=20, primary_key=True, verbose_name='Código')
    nombre_juego = models.CharField(max_length=50, verbose_name='Nombre')
    descripcion_juego = models.CharField(max_length=200, verbose_name='Descripción')
    url_img_juego = models.CharField(max_length=50, verbose_name='URL imagen')
    precio_juego = models.IntegerField(verbose_name="Precio")
    id_categoria = models.ForeignKey(CategoriaJuego, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_categoria

