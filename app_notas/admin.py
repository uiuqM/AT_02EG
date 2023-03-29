from django.contrib import admin

from .models import nota, usuario_nota, Usuario

# Register your models here.
admin.site.register(nota)
admin.site.register(Usuario)
admin.site.register(usuario_nota)