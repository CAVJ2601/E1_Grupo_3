from .views import home, inicioSesion, form_crea_usuario, form_login, categoria, lista_categorias, form_mod_categoria, form_del_categoria, form_crea_categoria
from django.urls import path

urlpatterns = [
    path('',home,name="home"),
    path('inicioSesion',inicioSesion,name="inicioSesion"),
    path('form_crea_usuario',form_crea_usuario,name="form_crea_usuario"),
    path('form_login',form_login,name="form_login"),
    path('lista_categorias',lista_categorias,name="lista_categorias"),
    path('categoria/<id>/<nombre>',categoria,name="categoria"),
    path('form_crea_categoria',form_crea_categoria,name="form_crea_categoria"),
    path('form_mod_categoria/<id>',form_mod_categoria,name="form_mod_categoria"),
    path('form_del_categoria/<id>',form_del_categoria,name="form_del_categoria"), 
    ]
