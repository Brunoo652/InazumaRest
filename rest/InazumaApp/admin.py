from django.contrib import admin
from .models import Jugador
from .models import Objeto
from .models import Stat


admin.site.register(Jugador)
admin.site.register(Objeto)
admin.site.register(Stat)
