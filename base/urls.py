from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name="Domovskástránka"),
    path('Infoomě/', views.Me, name="Me"),
    path('pracovnizkusenosti/', views.Pracovnizkus, name="pracovnizkusenosti"),
    path('Studium/', views.Studium, name="Studium"),
    path('Vlastnosti/', views.Vlastnosti, name="Vlastnosti"),
    path('Zajmy/', views.Zajmy, name="Zajmy"),
]
  