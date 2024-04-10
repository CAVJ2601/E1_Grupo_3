from django.shortcuts import render, redirect
from .models import Vehiculo
from .forms import VehiculoForm

# Create your views here.

def home(request):
    return render(request, "core/home.html")

def inicioSesion(request):
    return render(request, "core/inicioSesion.html")

def accion(request):
    return render(request, "core/accion.html")

def deportes(request):
    return render(request, "core/deportes.html")

def freeToPlay(request):
    return render(request, "core/freeToPlay.html")

def mmorpg(request):
    return render(request, "core/mmorpg.html")

def rpg(request):
    return render(request, "core/rpg.html")

def test(request):
    contexto = {"nombre":"Rodrigo Rojas"}
    return render(request,"core/test.html",contexto)

from django.shortcuts import render
from .models import Vehiculo
from .forms import VehiculoForm
from django.shortcuts import render, redirect


# Create your views here.


def home_vehiculo(request):
    vehiculos = Vehiculo.objects.all()
    datos = {
        'vehiculos':vehiculos
    }
    return render(request, 'core/home.html',datos)

def form_vehiculo(request):
    datos = {
        'form': VehiculoForm()
    }
    if request.method == 'POST':
        formulario = VehiculoForm(request.POST, request.FILES)
        print("Contenido de request.FILES:", request.FILES)
        print("Contenido de request.POST:", request.POST)
        if formulario.is_valid():  # Asegúrate de llamar a is_valid() correctamente
            formulario.save()
            datos['mensaje'] = "Guardado correctamente"
    return render(request, 'core/form_vehiculo.html', datos)

def form_mod_vehiculo(request, id):
    vehiculo = Vehiculo.objects.get(patente=id)
    datos = {'form': VehiculoForm(instance=vehiculo)}
    if request.method == 'POST':
        
        formulario = VehiculoForm(request.POST, request.FILES, instance=vehiculo)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Modificado correctamente"
    return render(request, 'core/form_mod_vehiculo.html', datos)

def form_del_vehiculo(request, id):
    # Obtener el vehículo a eliminar
    vehiculo = Vehiculo.objects.get(patente=id)

    # Verificar si se recibió una solicitud POST (es decir, se envió el formulario de confirmación de eliminación)
    if request.method == 'POST':
        # Eliminar el vehículo de la base de datos
        vehiculo.delete()
        # Redirigir a una página de éxito o a cualquier otra página deseada
        return redirect('/')

    # Si la solicitud no es POST, significa que se está mostrando el formulario de confirmación de eliminación
    # Renderizar la plantilla del formulario de confirmación de eliminación
    return render(request, 'core/form_del_vehiculo.html', {'vehiculo': vehiculo})
