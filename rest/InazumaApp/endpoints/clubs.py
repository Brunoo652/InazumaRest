from django.http import JsonResponse
from InazumaApp.models import Club, JugadorClubTemporada, Jugador


# club por id
def clubsByID(request, cid):
    clubs_get = Club.objects.get(id=cid)

    jugadores=[]
    for i in JugadorClubTemporada.objects.all():
        if cid == i.id:
            jugadores.append({"nombre": i.jugador.nombre, "sprite": i.jugador.sprite})

    return JsonResponse({
        "nombre": clubs_get.nombre,
        "sprite": clubs_get.logo,
        "jugadores": jugadores
    })
