from django.http import JsonResponse
from InazumaApp.models import Jugador, Stat, JugadorSupertecnica, Supertecnica
from django.db.models import Q


#Jugadores por nombre
def playersSearch(request):
    search_name = request.GET.get('search')

    if search_name is None:
        return JsonResponse({"message": "No existe el jugador"})

    search_letra = Jugador.objects.filter(Q(nombre__icontains=search_name) | Q(desc__icontains=search_name))

    j = []
    for p in search_letra:
        e = {
            "id": p.id,
            "name": p.nombre,
            "sprite": p.sprite
        }
        j.append(e)

    return JsonResponse(j, safe=False)


#Jugadores por id
def playersByID(request, pid):
    players_get = Jugador.objects.get(id=pid)
    players_stats = Stat.objects.filter(jugador=players_get)

    # crear un diccionario
    supertecnicas = []
    for i in JugadorSupertecnica.objects.all():
        if pid == i.id:
            supertecnicas.append({"nombre": i.supertecnica.nombre, "tipo": i.supertecnica.tipo, "afinidad": i.supertecnica.afinidad })
           # print(i.supertecnica)

    return JsonResponse({
        "nombre": players_get.nombre,
        "sprite": players_get.sprite,
        "desc": players_get.desc,
        "afinidad": players_get.afinidad,
        "sexo": players_get.sexo,
        "supertecnicas": supertecnicas,
        "stats": [{
            "PE": players_stats.get(nombre="PE").valor,
            "PT": players_stats.get(nombre="PT").valor,
            "T": players_stats.get(nombre="T").valor,
            "C": players_stats.get(nombre="C").valor,
            "d": players_stats.get(nombre="D").valor,
            "R": players_stats.get(nombre="R").valor,
            "A": players_stats.get(nombre="A").valor,
            "V": players_stats.get(nombre="V").valor,
            "S": players_stats.get(nombre="S").valor,
            "L": players_stats.get(nombre="L").valor
        }]
    })
