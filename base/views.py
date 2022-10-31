from django.shortcuts import render
from .models import Room
from .forms import RoomForm

def Home(request):
    context = {'infoome': infoome , 'prac': prac, 'stud': stud, 'vlas': vlas, 'zaj': zaj, 'nab': nab}
    return render(request, 'base/home.html', context)


def Me(request, pk):
    me = None
    for i in infoome:
        if i['id'] == int(pk):
            me = i
    context = {'me': me}
    return render(request, 'Infoome.html', context)


def Pracovnizkus(request, pk):
    Prac = None
    for i in prac:
        if i['id'] == int(pk):
            Prac = i
    context = {'Prac': Prac}
    return render(request, 'Pracovnizkusenosti.html', context)


def Studium(request, pk):
    Studs = None
    for i in stud:
        if i['id'] == int(pk):
            Studs= i
    context = {'stud': stud}
    return render(request, 'Studium.html', context)


def Vlastnosti(request, pk):
    Vlas = None
    for i in vlas:
        if i['id'] == int(pk):
            Vlas = i
    context = {'Vlas': Vlas}
    return render(request, 'Vlastnosti.html', context)


def Zajmy(request, pk):
    Zajm = None
    for i in zaj:
        if i['id'] == int(pk):
            Zajm = i
    context = {'Zajm': Zajm}
    return render(request, 'Zájmy.html', context)


def Nabidky(request, pk):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'Nabidky.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'room.html', context)


def Vytvornabidku(request):
    form = RoomForm()
    context = {'form': form}
    return render(request, 'base/uprava_nabidky.html', context)


nab = [
    {'id':0, 'name': 'Seznam nabídek práce'},
]

infoome = [
    {'id':1, 'name': 'Základní informace o mé osobě.'},
]
prac = [
    {'id':2, 'name': 'Mé dosavadní pracovní zkušenosti.'},
]

stud= [
    {'id':3, 'name': 'Studium.'},
]

vlas = [
    {'id':4, 'name': 'Mé vlastnosti schopnosti.'},
]

zaj = [
    {'id':5, 'name': 'Mé zájmy.'},
]
# Create your views here.
