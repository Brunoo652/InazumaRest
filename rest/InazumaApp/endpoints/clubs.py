from django.http import JsonResponse
from InazumaApp.models import Club, JugadorClubTemporada, Jugador


# club por id
def clubsByID(request, cid):
    clubs_get = Club.objects.get(id=cid)
   # print(clubs_get)

    jugadores=[]
    for i in JugadorClubTemporada.objects.all():
        if i.club == clubs_get:
            jugadores.append({"nombre": i.jugador.nombre, "sprite": i.jugador.sprite})
      #      print(i.jugador)

      #  print(cid)
      #  print(i.club)

    return JsonResponse({
        "nombre": clubs_get.nombre,
        "sprite": clubs_get.logo,
        "jugadores": jugadores
    })
