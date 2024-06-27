from django import forms
from . models import Usuario

from django.forms import ModelForm

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ["nombre","apellido","fec_nac","direccion","user_name","password","correo"]
        labels = {'nombre':'Nombre', 'fec_nac':'Fecha nacimiento', 'direccion':'Dirección', 'user_name':'Nombre usuario','password':'Contraseña'}