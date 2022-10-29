from django.contrib import admin

# Register your models here.

from .models import Room, Typ, Message


admin.site.register(Room)
admin.site.register(Typ)
admin.site.register(Message)