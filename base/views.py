from multiprocessing import context
from django.shortcuts import render

def Home(request):
    context = {'infoome': infoome , 'prac': prac, 'stud': stud, 'vlas': vlas, 'zaj': zaj, 'nab': nab}
    return render(request, 'base/home.html', context)


def Me(request, pk):
    me = None
    for i in infoome:
        if i['id'] == int(pk):
            me = 1
    context = {'me': me}
    return render(request, 'Infoome.html', context)


def Pracovnizkus(request, pk):
    Prac = None
    for i in prac:
        if i['id'] == int(pk):
            Prac = 1
    context = {'Prac': Prac}
    return render(request, 'Pracovnizkusenosti.html', context)


def Studium(request, pk):
    Studs = None
    for i in stud:
        if i['id'] == int(pk):
            Studs= 1
    context = {'stud': stud}
    return render(request, 'Studium.html', context)


def Vlastnosti(request, pk):
    Vlas = None
    for i in vlas:
        if i['id'] == int(pk):
            Vlas = 1
    context = {'Vlas': Vlas}
    return render(request, 'Vlastnosti.html', context)


def Zajmy(request, pk):
    Zajm = None
    for i in zaj:
        if i['id'] == int(pk):
            Zajm = 1
    context = {'Zajm': Zajm}
    return render(request, 'Zájmy.html', context)


def Nabidky(request, pk):
    Nabid = None
    for i in nab:
        if i['id'] == int(pk):
            Nabid = 1
    context = {'Nabid': Nabid}
    return render(request, 'Nabidky.html', context)


nab = [
    {'id':0, 'name': 'Nabídky Práce'},
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
