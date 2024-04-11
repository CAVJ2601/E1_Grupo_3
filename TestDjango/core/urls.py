from .views import home, inicioSesion, deportes, accion, freeToPlay, mmorpg, rpg, form_crea_usuario
from django.urls import path

urlpatterns = [
    path('',home,name="home"),
    path('inicioSesion',inicioSesion,name="inicioSesion"),
    path('deportes',deportes,name="deportes"),
    path('freeToPlay',freeToPlay,name="freeToPlay"),
    path('accion',accion,name="accion"),
    path('mmorpg',mmorpg,name="mmorpg"),
    path('rpg',rpg,name="rpg"),
    path('form_crea_usuario',form_crea_usuario,name="form_crea_usuario"),
    
    ]
