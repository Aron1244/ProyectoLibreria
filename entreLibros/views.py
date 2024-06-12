from django.shortcuts import render

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

def login(request):
    context={}
    return render(request, 'entreLibros/login.html', context)

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