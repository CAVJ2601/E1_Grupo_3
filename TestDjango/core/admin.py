from django.contrib import admin
from .models import Usuario, CategoriaJuego, Juego, Perfil

# Register your models here.

admin.site.register(Usuario)
admin.site.register(CategoriaJuego)
admin.site.register(Juego)
admin.site.register(Perfil)
