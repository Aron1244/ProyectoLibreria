from django.urls import path
from . import views

urlpatterns = [
    path('index.html', views.index, name='index'),
    path('catalogo.html', views.catalogo, name='catalogo'),
    path('contacto.html', views.contacto, name='contacto'),
    path('carrito.html', views.carrito, name='carrito'),
    path('crearUsuario.html', views.crearUsuario, name='crearUsuario'),
    path('login.html', views.custom_login_view, name='login'),
    path('libroA1.html', views.libroA1, name='libroA1'),
    path('libroA2.html', views.libroA2, name='libroA2'),
    path('libroA3.html', views.libroA3, name='libroA3'),
    path('libroB1.html', views.libroB1, name='libroB1'),
    path('libroB2.html', views.libroB2, name='libroB2'),
    path('libroB3.html', views.libroB3, name='libroB3'),
]
