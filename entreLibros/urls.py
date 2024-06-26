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
    path('admin.html', views.admin, name='admin'),
    path('crud_usuarios', views.crud_usuarios, name='crud_usuarios'),
    path('usuariosAdd', views.usuariosAdd, name='usuariosAdd'),
    path('usuarios_del/<str:pk>',views.usuarios_del,name='usuarios_del'),
    path('usuarios_edit/<str:pk>',views.usuarios_edit,name='usuarios_edit'),
    path('crud_categoria', views.crud_categoria, name='crud_categoria'),
    path('categoriaAdd', views.categoriaAdd, name='categoriaAdd'),
    path('categoria_del/<str:pk>',views.categoria_del,name='categoria_del'),
    path('categoria_edit/<str:pk>',views.categoria_edit,name='categoria_edit'),
    #libro por cierto me fije que cuando estamos en crudlibro el cambio de tema no funciona
    path('crudlibro', views.crudlibro, name='crudlibro'),
    path('addlibro', views.addlibro, name='addlibro'),
    path('libro_del/<str:pk>', views.libro_del, name='libro_del'),
    path('libro_Edit/<str:pk>', views.libro_Edit, name='libro_Edit'),
    

]
