from django.contrib import admin
from vrp import models

__author__ = 'gadzhi'

admin.site.register(models.Depot)
admin.site.register(models.Station)
admin.site.register(models.Edge)
admin.site.register(models.Network)
admin.site.register(models.Vehicle)
admin.site.register(models.Order)
