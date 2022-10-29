from django.contrib import admin

# Register your models here.

from .models import Nabidky,Room

admin.site.register(Nabidky)
admin.site.register(Room)