from django.shortcuts import render

def Home(request):
    return render(request, 'home.html')


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
# Create your views here.
