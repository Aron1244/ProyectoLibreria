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
        username = request.POST['username']
        password = request.POST['password']
        
        # Autenticar al usuario
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('/admin/')  # Redirigir al panel de administración de Django
            else:
                return redirect('/')  # Redirigir a la página de inicio (o cualquier otra página para usuarios regulares)
        else:
            # Mensaje de depuración
            print(f"Failed login attempt with username: {username} and password: {password}")
            return render(request, 'entreLibros/login.html', {'error': 'Usuario o contraseña incorrectos.'})
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