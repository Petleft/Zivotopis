from django.urls import path
from . import views

#setup url mapping for our website 
urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    path('', views.Home, name="Domovskástránka"),
    path('Infoomě/<str:pk>/', views.Me, name="Infoomě"),
    path('pracovnizkusenosti/<str:pk>/', views.Pracovnizkus, name="pracovnizkusenosti"),
    path('Studium/<str:pk>/', views.Studium, name="Studium"),
    path('Vlastnosti/<str:pk>/', views.Vlastnosti, name="Vlastnosti"),
    path('Zajmy/<str:pk>/', views.Zajmy, name="Zajmy"),
    path('Nabidky/<str:pk>/', views.Nabidky, name="Nabidkyprace"),
    path('Nabidky/room/<str:pk>', views.room, name="room"),
    path('create-room/', views.Vytvornabidku, name="Vytvoreninabidky"),
    path('update-room/<str:pk>/', views.Upraveninabidky, name="Upraveninabidky"),
    path('delete-room/<str:pk>/', views.Smazaninabidky, name="Smazaninabidky"),
]
  