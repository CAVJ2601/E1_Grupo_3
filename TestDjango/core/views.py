from .forms import UsuarioForm, LoginForm, CategoriasForm
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

def categoria(request, id, nombre):
    print("id " + id)
    print("nombre " + nombre)
    juegos = Juego.objects.filter(id_categoria=id)
    datos = {
        'nombre':nombre,
        'juegos':juegos
    }

    return render(request, "core/categoria.html", datos)

def lista_categorias(request):

    categorias = CategoriaJuego.objects.all().order_by('id_categoria')
    print("cantidad de categorias")
    print(categorias.count())
    datos = {
        'categorias':categorias
    }
    return render(request, "core/lista_categorias.html", datos)


def form_mod_categoria(request, id):

    categoria = CategoriaJuego.objects.get(id_categoria=id)
    print("cantidad a modificar")
    print(id)
    datos = {
        'form':CategoriasForm(instance=categoria),
    }
    if request.method == 'POST':
        formulario = CategoriasForm(request.POST, request.FILES, instance=categoria)
        formulario.save()
        return redirect('/lista_categorias')
        
    return render(request, 'core/form_mod_categoria.html', datos)

def form_del_categoria(request, id):

    categoria = CategoriaJuego.objects.get(id_categoria=id)
    print("id a borrar")
    print(id)

    if request.method == 'POST':
        categoria.delete()
       
        return redirect('/lista_categorias')
    
    return render(request, 'core/form_del_categoria.html', {'categoria':categoria})

def form_crea_categoria(request):
    datos = {
        'form': CategoriasForm()
    }
    print("Entrando a vista crea categoria")
    if request.method == 'POST':
        formulario = CategoriasForm(request.POST, request.FILES)
        if formulario.is_valid(): 
            print("Formulario correcto")
            formulario.save()
            datos['mensaje'] = "Guardado correctamente"
        else: 
            datos['mensaje'] = "Error " + formulario.errors.as_text()
        
    return render(request, 'core/form_crea_categoria.html', datos)

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
