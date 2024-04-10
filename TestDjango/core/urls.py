from .views import home, test, inicioSesion, deportes, accion, freeToPlay, mmorpg, rpg, home_vehiculo, form_vehiculo, form_mod_vehiculo, form_del_vehiculo
from django.urls import path

urlpatterns = [
    path('',home,name="home"),
    path('test',test,name="test"),
    path('inicioSesion',inicioSesion,name="inicioSesion"),
    path('deportes',deportes,name="deportes"),
    path('freeToPlay',freeToPlay,name="freeToPlay"),
    path('accion',accion,name="accion"),
    path('mmorpg',mmorpg,name="mmorpg"),
    path('rpg',rpg,name="rpg"),
    path('home-vehiculo',home_vehiculo,name="home_vehiculo"),
    path('form-vehiculo',form_vehiculo,name="form_vehiculo"),
    path('form-mod-vehiculo/<id>',form_mod_vehiculo,name="form_mod_vehiculo"),
    path('form-del-vehiculo/<id>',form_del_vehiculo,name="form_del_vehiculo"),
    ]
