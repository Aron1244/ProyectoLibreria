from django.contrib import admin
from . models import Usuario,Libro,Categoria

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Libro)
admin.site.register(Categoria)