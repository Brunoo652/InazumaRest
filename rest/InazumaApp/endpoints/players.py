from django.http import JsonResponse
from InazumaApp.models import Jugador, Stat, JugadorSupertecnica, Supertecnica
from django.db.models import Q


def playersSearch(request):
    search_name = request.GET.get('search')
    if search_name is None:
        print("No existe el jugador")

    else:
        print(search_name)
    """"
        search_afinidad = request.GET.get('afinidad')
        if search_afinidad is None:
            print("No existe la afinidad")
    
        else:
            print(search_afinidad)
    """
    # todos los jugadores q tienen la busquda en el nombre o descripcion
    search_letra = Jugador.objects.filter(Q(nombre__icontains=search_name) | Q(desc__icontains=search_name))
    print(search_letra)

    # meter los datos en un JSON
    j = []
    for p in search_letra:
        print(p)
        print(p.nombre)
        print(p.id)
        print(p.sprite)
        # crear un diccionario
        e = {
            "id": p.id,
            "name": p.nombre,
            "sprite": p.sprite
        }
        print(e)
        j.append(e)

    # todos los jugadores
    all_players = Jugador.objects.all()
    print(all_players)

    # todos los jugadores llamados Mark Evans TEST
    player_for_name = Jugador.objects.filter(nombre="Mark Evans TEST")
    print(player_for_name)

    # Todos los jugadores con Ma en sus nombres
    players_filtered = Jugador.objects.filter(nombre__icontains="Ma")
    print(players_filtered)

    # todos los jugadores con afinidad montaña
    players_afinidad = Jugador.objects.filter(afinidad="A")
    print(players_afinidad)

    # Todos los jugadores con afinidad montaña y nombre
    players_afinidad_nombre = Jugador.objects.filter(afinidad__icontains="M", nombre__icontains="Ma")
    print(players_afinidad_nombre)

    # todas las descripciones
    todas_descripciones = Jugador.objects.filter(desc__icontains="oekgwpobrkm")
    print(todas_descripciones)

    # todos los nombres y descricpciones q contengan al menos una letra igual
    jugadores_descripciones = Jugador.objects.filter(Q(nombre__icontains="M") | Q(desc__icontains="M"))
    print(jugadores_descripciones)

    return JsonResponse(j, safe=False)


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
