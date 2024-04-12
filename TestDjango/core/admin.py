from django.contrib import admin
from .models import Usuario, CategoriaJuego, Juego

# Register your models here.

admin.site.register(Usuario)
admin.site.register(CategoriaJuego)
admin.site.register(Juego)
