from django.shortcuts import render, redirect
from .forms import UsuarioForm

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

#from django.shortcuts import render
from .forms import UsuarioForm
from django.shortcuts import render, redirect


# Create your views here.

def form_crea_usuario(request):
    datos = {
        'form': UsuarioForm()
    }
    print("Entrando a vista crea usuario")
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST, request.FILES)
        if formulario.is_valid(): 
            print("Formulario correcto")
            formulario.save()
            datos['mensaje'] = "Guardado correctamente"
        else: 
            datos['mensaje'] = "Error " + formulario.errors.as_text()
        
    return render(request, 'core/form_crea_usuario.html', datos)
