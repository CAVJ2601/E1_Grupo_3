from .views import home, form_crea_usuario, form_login, categoria, lista_categorias, form_mod_categoria, form_del_categoria, form_crea_categoria, lista_juegos, lista_juegos_por_encargo, form_mod_juego, form_del_juego, form_crea_juego, cerrar_sesion, perfil_usuario
from django.urls import path

urlpatterns = [
    path('',home,name="home"),
    path('form_crea_usuario',form_crea_usuario,name="form_crea_usuario"),
    path('form_login',form_login,name="form_login"),
    path('cerrar_sesion',cerrar_sesion,name="cerrar_sesion"),
    path('categoria/<id>/<nombre>',categoria,name="categoria"),
    path('lista_categorias',lista_categorias,name="lista_categorias"),
    path('form_crea_categoria',form_crea_categoria,name="form_crea_categoria"),
    path('form_mod_categoria/<id>',form_mod_categoria,name="form_mod_categoria"),
    path('form_del_categoria/<id>',form_del_categoria,name="form_del_categoria"), 
    path('lista_juegos',lista_juegos,name="lista_juegos"),
    path('lista_juegos_por_encargo',lista_juegos_por_encargo,name="lista_juegos_por_encargo"),
    path('form_crea_juego',form_crea_juego,name="form_crea_juego"),
    path('form_mod_juego/<id>',form_mod_juego,name="form_mod_juego"),
    path('form_del_juego/<id>',form_del_juego,name="form_del_juego"), 
    path('perfil_usuario',perfil_usuario, name="perfil_usuario"),
    ]
