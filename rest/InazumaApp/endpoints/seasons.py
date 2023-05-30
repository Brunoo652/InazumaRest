from django.http import JsonResponse
from InazumaApp.models import Temporada, JugadorClubTemporada


def seasonsByID(request, sid):
    seasons_get = Temporada.objects.get(id=sid)
    #print(seasons_get)

    clubes = []
    for i in JugadorClubTemporada.objects.all():
        if i.club == seasons_get:
            clubes.append({"nombre": i.club.nombre, "logo": i.club.logo})

    return JsonResponse({
        "nombre": seasons_get.nombre,
        "clubs": clubes
    })
