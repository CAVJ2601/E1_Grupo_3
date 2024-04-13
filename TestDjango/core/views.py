from .forms import UsuarioForm, LoginForm, CategoriasForm, JuegoForm 
from .models import Usuario, CategoriaJuego, Juego, Perfil
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def home(request):
    usuario_conectado = request.session.get('user', '')
    role = request.session.get('role', '1')

    categorias = CategoriaJuego.objects.all()
    datos = {
        'categorias':categorias,
        'usuario_conectado':usuario_conectado,
        'role':role
    }
    print("Rol en home " + role)
    return render(request, "core/home.html", datos)

def cerrar_sesion(request):
    request.session['user'] = ''
    request.session['role'] = '1'
    return render(request, "core/cerrar_sesion.html")

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
            return redirect('/lista_categorias')
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

    request.session['user'] = ''
    request.session['role'] = '1'

    datos = {
        'form': LoginForm(),
        'perfil':''
    }
    print("Entrando a vista login")
    if request.method == 'POST':
        formulario = LoginForm(request.POST, request.FILES)
        data = request.POST
        usuario_form = data.get('usuario')
        clave_form = data.get('password')
        
        print("usuario_form " + usuario_form)
        print("clave_form " + clave_form)
        
        try:
            user = Usuario.objects.get(usuario=usuario_form)
        

            clave = user.password
            role = user.id_perfil.id_perfil
            print("clave " + clave)



            print("Formulario correcto")
            if clave == clave_form:
                print("clave correcta " + clave)
                datos['mensaje'] = "Clave correcta"
                request.session['user'] = usuario_form
                request.session['role'] = role
                print("Role " + role)
                datos['role'] = role
            else:
                print("clave incorrecta" + clave)
                datos['mensaje'] = "Clave incorrecta"

        except ObjectDoesNotExist:
            datos['mensaje'] = "Usuario no existe, por favor regístrese"

        
    return render(request, 'core/form_login.html', datos)

def lista_juegos(request):

    juegos = Juego.objects.all().order_by('id_juego')
    print("cantidad de juegos")
    print(juegos.count())
    datos = {
        'juegos':juegos
    }
    return render(request, "core/lista_juegos.html", datos)


def form_mod_juego(request, id):

    juego = Juego.objects.get(id_juego=id)
    print("juego a modificar")
    print(id)
    datos = {
        'form':JuegoForm(instance=juego),
    }
    if request.method == 'POST':
        formulario = JuegoForm(request.POST, request.FILES, instance=juego)
        formulario.save()
        return redirect('/lista_juegos')
        
    return render(request, 'core/form_mod_juego.html', datos)

def form_del_juego(request, id):

    juego = Juego.objects.get(id_juego=id)
    print("id a borrar")
    print(id)

    if request.method == 'POST':
        juego.delete()
       
        return redirect('/lista_juegos')
    
    return render(request, 'core/form_del_juego.html', {'juego':juego})

def form_crea_juego(request):
    datos = {
        'form': JuegoForm()
    }
    print("Entrando a vista crea juego")
    if request.method == 'POST':
        formulario = JuegoForm(request.POST, request.FILES)
        if formulario.is_valid(): 
            print("Formulario correcto")
            formulario.save()
            datos['mensaje'] = "Guardado correctamente"
            return redirect('/lista_juegos')
        else: 
            datos['mensaje'] = "Error " + formulario.errors.as_text()
        
    return render(request, 'core/form_crea_juego.html', datos)
