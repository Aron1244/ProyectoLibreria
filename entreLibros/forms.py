from django import forms
from . models import Usuario,Categoria,Libro

from django.forms import ModelForm

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ["nombre","apellido","fec_nac","direccion","user_name","password","correo"]
        labels = {'nombre':'Nombre', 'fec_nac':'Fecha nacimiento', 'direccion':'Dirección', 'user_name':'Nombre usuario','password':'Contraseña'}

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ["nombre_categoria",]
        labels = {'nombre_categoria':'Categoría', }



class Libroform(ModelForm):
    class Meta:
        model = Libro
        fields = ["nombre_libro","autor","saga","nro_pag","isbn","encuadernacion", "dimensiones","precio","categoria","portada","cantidad"]
        labels = {'nombre_libro':'Nombre','autor': 'Autor', 'saga':'Saga','nro_pag':'N° Páginas','isbn':'ISBN','encuadernacion':'Encuadernación','dimensiones': 'Dimensiones','precio': 'Precio','Categoria':'Categoría','Portada':'Portada'}