from django.contrib import admin

from .models import Categoria
from .models import Helado
from .models import Alimento

# Autor: EDIS

admin.site.register(Categoria)
admin.site.register(Helado)
admin.site.register(Alimento)
