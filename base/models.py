from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Nabidky(models.Model):
    #host = 
    #topic =
    name = models.CharField(max_Length=200)
    description = models.TextField(null=True, blank=True)
    #participants =
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name