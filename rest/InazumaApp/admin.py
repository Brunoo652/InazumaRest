from django.contrib import admin
from .models import Jugador
from .models import Objeto
from .models import Stat
from .models import Supertecnica
from .models import JugadorSupertecnica


admin.site.register(Jugador)
admin.site.register(Objeto)
admin.site.register(Stat)
admin.site.register(Supertecnica)
admin.site.register(JugadorSupertecnica)
