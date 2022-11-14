from django.contrib import admin

# Register your models here.

from .models import Room, Typ, Plath, Platm, Hodinyd, Hodinym, typprace

#setup admin page what will show in admin pannels
admin.site.register(Room)
admin.site.register(Typ)
admin.site.register(Platm)
admin.site.register(Plath)
admin.site.register(Hodinyd)
admin.site.register(Hodinym)
admin.site.register(typprace)
