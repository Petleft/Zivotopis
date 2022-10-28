from django.shortcuts import render

def Home(request):
    context = {'infoome': infoome , 'prac': prac, 'stud': stud, 'vlas': vlas, 'zaj': zaj}
    return render(request, 'home.html', context)


def Me(request):
    return render(request, 'Infoome.html')


def Pracovnizkus(request):
    return render(request, 'Pracovnizkusenosti.html')


def Studium(request):
    return render(request, 'Studium.html')


def Vlastnosti(request):
    return render(request, 'Vlastnosti')


def Zajmy(request):
    return render(request, 'Zájmy.html')


# def room(request):
 #   return render(request, 'room.html')


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
