from django.db import models

# Create your models here.

class Perfil(models.Model):
    id_perfil = models.CharField(max_length=20, primary_key=True, verbose_name='Código perfil')
    nombre_perfil = models.CharField(max_length=50, verbose_name='Nombre perfil')

    def __str__(self):
        return self.nombre_perfil
    
class Region(models.Model):
    id_region = models.CharField(max_length=20, primary_key=True, verbose_name='Código región')
    nombre_region = models.CharField(max_length=50, verbose_name='Nombre región')

    def __str__(self):
        return self.nombre_region
    
class Comuna(models.Model):
    id_comuna = models.CharField(max_length=20, primary_key=True, verbose_name='Código comuna')
    nombre_comuna = models.CharField(max_length=50, verbose_name='Nombre comuna')
    id_region = models.ForeignKey(Region, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_comuna

class Usuario(models.Model):
    usuario = models.CharField(max_length=20, primary_key=True, verbose_name='Nombre usuario')
    nombre = models.CharField(max_length=50, verbose_name='Nombre completo')
    correo = models.CharField(max_length=50,verbose_name='Correo electronico')
    password = models.CharField(max_length=20,verbose_name='Password')
    fecha_nac = models.DateField(verbose_name='Fecha de nacimiento')
    direccion = models.CharField(max_length=100,verbose_name='Dirección despacho')
    id_perfil = models.ForeignKey(Perfil, default="1", on_delete=models.CASCADE)
    id_region = models.ForeignKey(Region, null=True, on_delete=models.CASCADE)
    id_comuna = models.ForeignKey(Comuna, null=True, on_delete=models.CASCADE)

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
    imagen_juego = models.ImageField(upload_to='imagenes/', null=True, verbose_name='Imagen del juego')

    def __str__(self):
        return self.nombre_juego

