from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, response

from .models import *

from rest_framework.decorators import api_view
from rest_framework.response import Response
# from .serializers import BigyoSerializer


@login_required
def index(request):
    return render(request, "index.html", {})

@login_required
def csoportok(request):
    return render(request, "linkek.html", {'linkek': request.user.felhasznalo.csoportjai()})

@login_required
def dolgozatok(request, csoport):
    a_csoport = Csoport.objects.get(urlkod=csoport)
    return render(request, "linkek.html", {'linkek': a_csoport.dolgozatai(request.user)})

@login_required
def milegyen(request, csoport, dolgozat):
    a_csoport = Csoport.objects.get(urlkod=csoport)
    a_dolgozat = Dolgozat.objects.get(urlkod=dolgozat)
    linkek = [
        {
            'nev': 'Megtekintés', 
            'urlkod':'view'
        },
        {
            'nev': 'Módosítás', 
            'urlkod':'edit'
        },
    ]
    return render(request, "linkek.html", {'linkek': linkek})

@login_required
def dolgozat_megtekintese(request, csoport, dolgozat):
    a_csoport = Csoport.objects.get(urlkod=csoport)
    a_dolgozat = Dolgozat.objects.get(urlkod=dolgozat)
    return render(request, "dolgozat.html", {
        'csoport': a_csoport,
        'dolgozat':a_dolgozat,
        })

def dolgozat_szerkesztese(request, csoport, dolgozat):
    a_csoport = Csoport.objects.get(urlkod=csoport)
    a_dolgozat = Dolgozat.objects.get(urlkod=dolgozat)
    return render(request, "linkek.html", {})



"""

#Az api_view annyit csinál, hogy behozza ezt a szép gyári api-t, ami debughoz elég jól jöhet
@api_view(['GET'])
def api_get_var(request):
    szotar = {
        'a': 7,
        'b':'blabla',
        }
    return Response(szotar)

# objektumokat serializálni kell, hogy frontenden kezelni lehessen. Ehhez az objektumokhoz létre kell hozni egy személyre szóló serializert. 
# Ennek a konstruktora majd a következőképpen fog működni.

# BigyoSerializer(object, request.data) a következőképpen működik:

# - CREATE: Ha csak "request.data" van, akkor az egy CREATE: létrehozza a modellben a megfelelő objektumot.
# - READ ALL: Ha csak "object.all()" van és "many=True", akkor visszaadja az összes objektum szerializáltját
# - READ ONE: Ha csak konkrét "object" van és "many=False", akkor visszaadja a megadtott objektum szerializáltját
# - UPDATE: Ha konkrét objektum és "request.data" is van, akkor az egy UPDATE: módosítja a request alapján az objektumot.
# (- DELETE: törléshez nem kell serializer)


# - CREATE: Ha csak "request.data" van, akkor az egy CREATE: létrehozza a modellben a megfelelő objektumot.
@api_view(['POST'])
def api_create(request):
    serializer = BigyoSerializer(
        data=request.data # értelmezi a változtatást
        )

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# - READ ALL: Ha csak "object.all()" van és "many=True", akkor visszaadja az összes objektum szerializáltját
@api_view(['GET'])
def api_get_all(request):
    bigyok = Bigyo.objects.all()
    serializer = BigyoSerializer(bigyok, many = True)
    return Response(serializer.data)

# - READ ONE: Ha csak konkrét "object" van és "many=False", akkor visszaadja a megadtott objektum szerializáltját
@api_view(['GET'])
def api_get_one(request, pk):    
    bigyo = Bigyo.objects.get(id=pk)
    serializer = BigyoSerializer(bigyo, many = False)
    return Response(serializer.data)

# - UPDATE: Ha konkrét objektum és "request.data" is van, akkor az egy UPDATE: módosítja a request alapján az objektumot.
@api_view(['POST'])
def api_update(request, pk):
    bigyo = Bigyo.objects.get(id=pk)
    serializer = BigyoSerializer(
        instance=bigyo,  # beazonosítja az objektumot
        data=request.data # társítja a változtatást
        ) 

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# (- DELETE: törléshez nem kell serializer)
@api_view(['DELETE'])
def api_delete(request, pk):
    bigyo = Bigyo.objects.get(id=pk)
    bigyo.delete()
    return Response('ez bizony törölve lett')

"""