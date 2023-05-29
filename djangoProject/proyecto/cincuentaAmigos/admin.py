from django.contrib import admin

from .models import Categoria
from .models import Helado
from .models import Alimento
from .models import Mesa
from .models import Carrito
from .models import Votacion

admin.site.register(Categoria)
admin.site.register(Helado)
admin.site.register(Alimento)
admin.site.register(Mesa)
admin.site.register(Carrito)
admin.site.register(Votacion)
