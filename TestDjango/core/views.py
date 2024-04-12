from .forms import UsuarioForm, LoginForm
from .models import Usuario, CategoriaJuego, Juego
from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    categorias = CategoriaJuego.objects.all()
    datos = {
        'categorias':categorias
    }
    return render(request, "core/home.html", datos)

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

def categoria(request, id, nombre):
    print("id " + id)
    print("nombre " + nombre)
    juegos = Juego.objects.filter(id_categoria=id)
    datos = {
        'nombre':nombre,
        'juegos':juegos
    }

    return render(request, "core/categoria.html", datos)

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

def form_login(request):
    datos = {
        'form': LoginForm()
    }
    print("Entrando a vista login")
    if request.method == 'POST':
        formulario = LoginForm(request.POST, request.FILES)
        data = request.POST
        usuario_form = data.get('usuario')
        clave_form = data.get('password')

        print("usuario_form " + usuario_form)
        print("clave_form " + clave_form)
        user = Usuario.objects.get(usuario=usuario_form)

        clave = user.password
        print("clave " + clave)



        print("Formulario correcto")
        if clave == clave_form:
            print("clave correcta " + clave)
            datos['mensaje'] = "Clave correcta"
        else:
            print("clave incorrecta" + clave)
            datos['mensaje'] = "Clave incorrecta"

        
    return render(request, 'core/form_login.html', datos)
