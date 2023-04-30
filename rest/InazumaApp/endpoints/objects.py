from django.http import JsonResponse
from InazumaApp.models import Objeto
from django.db.models import Q


def ObjectsSearch(request):
    search_object = request.GET.get('search')
    if search_object is None:
        print("No existe el objeto")

    else:
        print(search_object)

    search_tipo = request.GET.get('tipo')
    if search_tipo is None:
        print("No existe la tipo de objeto")

    else:
        print(search_tipo)

    # todos los objetos q tienen la busquda en el nombre o descripcion
    #search_letra = Jugador.objects.filter(Q(nombre__icontains=search_name) | Q(desc__icontains=search_name))
    #print(search_letra)

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

    return JsonResponse(j, safe=False)