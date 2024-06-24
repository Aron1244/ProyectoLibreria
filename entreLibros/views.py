from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

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