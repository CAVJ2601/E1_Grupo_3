from django.urls import path
from . import views

#api/
urlpatterns = [
    path('regiones', views.lista_regiones, name='lista_regiones'),
    path('regiones/<id>', views.vista_regiones, name='vista_regiones'),
    path('comunas', views.lista_comunas, name='lista_comunas'),
    path('comunas/<id>', views.vista_comunas, name='vista_comunas'),
]