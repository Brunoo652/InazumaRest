from django.http import JsonResponse
from InazumaApp.models import Temporada


def seasonsSearch(request):
    search_nameT = request.GET.get('search')

    # todos las temporadas q tienen la busqueda en el nombre
    search_letraT = Temporada.objects.filter(nombre__icontains=search_nameT)
    #print(search_letraT)

    # meter los datos en un JSON
    j = []
    for i in search_letraT:
        k = {
            "nombre": i.nombre,
            "logo": i.logo
        }
        j.append(k)

    return JsonResponse(j, safe=False)


def seasonsByID(request, sid):
    pass
