from django.contrib import admin
from .models import Jugador
from .models import Objeto
from .models import Stat
from .models import Supertecnica
from .models import JugadorSupertecnica
from .models import Club
from .models import JugadorClubTemporada
from .models import Temporada


admin.site.register(Jugador)
admin.site.register(Objeto)
admin.site.register(Stat)
admin.site.register(Supertecnica)
admin.site.register(JugadorSupertecnica)
admin.site.register(Club)
admin.site.register(JugadorClubTemporada)
admin.site.register(Temporada)


