from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from . models import Usuario, Categoria

from . forms import UsuarioForm, CategoriaForm


# Create your views here.

def index(request):
    context={}
    return render(request, 'entreLibros/index.html', context)

def catalogo(request):
    context={}
    return render(request, 'entreLibros/catalogo.html', context)

def contacto(request):
    context={}
    return render(request, 'entreLibros/contacto.html', context)

def carrito(request):
    context={}
    return render(request, 'entreLibros/carrito.html', context)

def crearUsuario(request):
    context={}
    return render(request, 'entreLibros/crearUsuario.html', context)

def custom_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Autenticar al usuario
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if user.is_superuser:
                # Si es superusuario, redirigir al panel de administración de Django
                return redirect('/admin/')
            elif user.username == 'admin1':
                # Si el usuario es 'admin1', redirigir a una template personalizada de administrador
                print(f"Usuario {username} autenticado como admin1")
                return render(request, 'entreLibros/admin.html')
            else:
                # Si no es superusuario ni 'admin1', redirigir a la página de inicio
                return redirect('/')
        else:
            # Si la autenticación falla, mostrar mensaje de error
            error_message = 'Usuario o contraseña incorrectos.'
            return render(request, 'entreLibros/login.html', {'error': error_message})
    
    # Si el método de solicitud no es POST, simplemente renderiza el formulario de inicio de sesión
    return render(request, 'entreLibros/login.html')

def libroA1(request):
    context={}
    return render(request, 'entreLibros/libroA1.html', context)

def libroA2(request):
    context={}
    return render(request, 'entreLibros/libroA2.html', context)

def libroA3(request):
    context={}
    return render(request, 'entreLibros/libroA3.html', context)

def libroB1(request):
    context={}
    return render(request, 'entreLibros/libroB1.html', context)

def libroB2(request):
    context={}
    return render(request, 'entreLibros/libroB2.html', context)

def libroB3(request):
    context={}
    return render(request, 'entreLibros/libroB3.html', context)

def admin(request):
    context={}
    return render(request, 'entreLibros/admin.html', context)

# CRUD USUARIOS

def crud_usuarios(request):

    usuarios = Usuario.objects.all()
    context = {'usuarios': usuarios}
    print("Enviando datos usuarios_list")
    return render(request, 'entreLibros/usuarios_list.html', context)

def usuariosAdd(request):
    print("Estoy controlando usuariosAdd...")
    context={}

    if request.method == "POST":
        print("Controlador es un post...")
        form = UsuarioForm(request.POST)

        if form.is_valid:
            print("Estoy en agregar, is_valid")
            form.save()

            #limpiar forms
            form=UsuarioForm()

            context = {'mensaje':"Ok, datos grabados...", "form":form}
            return render(request, "entreLibros/usuarios_add.html",context)
        else:
            context = {'form':form}
    else:
        form = UsuarioForm()
        context = {'form':form}
        return render(request, 'entreLibros/usuarios_add.html',context)

def usuarios_del(request, pk):
    mensajes = []
    errores = []
    context = {}

    try:
        usuario = Usuario.objects.get(id_usuario=pk)
        usuario.delete()
        mensajes.append("Bien, datos eliminados...")
    except Usuario.DoesNotExist:
        errores.append("Error, id no existe")
    except Exception as e:
        errores.append(f"Error inesperado: {str(e)}")
    
    usuarios = Usuario.objects.all()
    context = {'usuarios': usuarios, 'mensajes': mensajes, 'errores': errores}
    return render(request, 'entreLibros/usuarios_list.html', context)


def usuarios_edit(request,pk):
    try:
        usuario = Usuario.objects.get(id_usuario=pk)
        context = {}
        if usuario:
            print("Edit encontro el usuario...")
            if request.method == "POST":
                print("Edit, es un POST")
                form = UsuarioForm(request.POST, instance=usuario)
                form.save()
                mensaje = "Bien, datos actualizados..."
                print(mensaje)
                context = {'usuario':usuario, 'form':form, 'mensaje':mensaje}
                return render(request, 'entreLibros/usuarios_edit.html', context)
            else:
                # no es un POST
                print("Edit, NO es un POST")
                form = UsuarioForm(instance=usuario)
                mensaje = ""
                context = {'usuario':usuario, 'form':form, 'mensaje':mensaje}
                return render(request, 'entreLibros/usuarios_edit.html', context)
    except:
        print("Error, id no existe...")
        usuarios = Usuario.objects.all()
        mensaje = "Error, id no existe"
        context = {'mensaje':mensaje, 'usuarios':usuarios}
        return render(request, 'entreLibros/usuarios_list.html', context)
    
# CRUD CATEGORIA

def crud_categoria(request):

    categorias = Categoria.objects.all()
    context = {'categorias': categorias}
    print("Enviando datos categorias_list")
    return render(request, 'entreLibros/categoria_list.html', context)

def categoriaAdd(request):
    print("Estoy controlando categoriaAdd...")
    context={}

    if request.method == "POST":
        print("Controlador es un post...")
        form = CategoriaForm(request.POST)

        if form.is_valid:
            print("Estoy en agregar, is_valid")
            form.save()

            #limpiar forms
            form=CategoriaForm()

            context = {'mensaje':"Ok, datos grabados...", "form":form}
            return render(request, "entreLibros/categoria_add.html",context)
        else:
            context = {'form':form}
    else:
        form = CategoriaForm()
        context = {'form':form}
        return render(request, 'entreLibros/categoria_add.html',context)

def categoria_del(request, pk):
    mensajes = []
    errores = []
    context = {}

    try:
        categoria = Categoria.objects.get(id_categoria=pk)
        categoria.delete()
        mensajes.append("Bien, datos eliminados...")
    except Categoria.DoesNotExist:
        errores.append("Error, id no existe")
    except Exception as e:
        errores.append(f"Error inesperado: {str(e)}")
    
    categorias = Categoria.objects.all()
    context = {'categorias': categorias, 'mensajes': mensajes, 'errores': errores}
    return render(request, 'entreLibros/categoria_list.html', context)


def categoria_edit(request,pk):
    try:
        categoria = Categoria.objects.get(id_categoria=pk)
        context = {}
        if categoria:
            print("Edit encontró la categoria...")
            if request.method == "POST":
                print("Edit, es un POST")
                form = CategoriaForm(request.POST, instance=categoria)
                form.save()
                mensaje = "Bien, datos actualizados..."
                print(mensaje)
                context = {'categoria':categoria, 'form':form, 'mensaje':mensaje}
                return render(request, 'entreLibros/categoria_edit.html', context)
            else:
                # no es un POST
                print("Edit, NO es un POST")
                form = CategoriaForm(instance=categoria)
                mensaje = ""
                context = {'categoria':categoria, 'form':form, 'mensaje':mensaje}
                return render(request, 'entreLibros/categoria_edit.html', context)
    except:
        print("Error, id no existe...")
        categorias = Categoria.objects.all()
        mensaje = "Error, id no existe"
        context = {'mensaje':mensaje, 'categorias':categorias}
        return render(request, 'entreLibros/categoria_list.html', context)