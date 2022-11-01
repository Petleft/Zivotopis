from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Typ(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Plath(models.Model):
    name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

    
class Platm(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Hodinyd(models.Model):
    name = models.CharField(max_length=5)

    def __str__(self):
        return self.name


class Hodinym(models.Model):
    name = models.CharField(max_length=5)

    def __str__(self):
        return self.name

class typprace(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

#class Room(models.Model):
#    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#    typprace = models.ForeignKey(Typ, on_delete=models.SET_NULL, null=True)
#    name = models.CharField(max_length=200)
#    plathodinovy = models.ForeignKey(Plath, on_delete=models.SET_NULL, null=True)
#    platmesicni = models.ForeignKey(Platm, on_delete=models.SET_NULL, null=True)
#    hodinyden = models.ForeignKey(Hodinyd, on_delete=models.SET_NULL, null=True)
#    hodinymesic = models.ForeignKey(Hodinym, on_delete=models.SET_NULL, null=True)
#    description = models.TextField(null=True, blank=True)
#    updated = models.DateTimeField(auto_now=True)
#    created = models.DateTimeField(auto_now_add=True)
# 
#
#    def __str__(self):
#        return self.name


class Room(models.Model):
    Zadávající = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    typ_práce = models.ForeignKey(typprace, on_delete=models.SET_NULL, null=True)
    Nazev_pozice = models.CharField(max_length=20)
    Hodinový_plat = models.CharField(max_length=10, blank=True)
    Měsíční_mzda = models.CharField(max_length=10, blank=True)
    Hodiny_za_den = models.CharField(max_length=10, blank=True)
    Hodiny_za_měsíc = models.CharField(max_length=10, blank=True)
    popis_práce = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.typ_práce


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]
