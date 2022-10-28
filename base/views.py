from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
    return HttpResponse("Home page")


def Me(request):
    return HttpResponse("Informace o mě")


def Pracovnizkus(request):
    return HttpResponse("Pracovní zkušenosti")


def Studium(request):
    return HttpResponse("Studium")


def Vlastnosti(request):
    return HttpResponse("Vlastnosti")


def Zajmy(request):
    return HttpResponse("Zájmy")
# Create your views here.
