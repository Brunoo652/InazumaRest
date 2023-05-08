from django.http import JsonResponse
from InazumaApp.models import Objeto
from django.db.models import Q


def objectsSearch(request):
    search_tipo = request.GET.get('tipo')
    if search_tipo is None:
        print("No existe la tipo de objeto")

    else:
        print(search_tipo)

    # todos los objetos q tienen la busquda en el nombre o descripcion
    search_letra = Objeto.objects.filter(tipo__icontains=search_tipo)
   # print(search_letra)

    # meter los datos en un JSON
    j = []
    for p in search_letra:
        print(p)
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


def objectById(request, oid):

    object_get = Objeto.objects.get(id=oid)

    return JsonResponse({
        "nombre": object_get.nombre,
        "sprite": object_get.sprite,
        "desc": object_get.desc,
        "obtencion": object_get.obtencion,
        "tipo": object_get.tipo
    })


