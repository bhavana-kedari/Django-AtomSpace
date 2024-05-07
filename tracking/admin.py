from django.contrib import admin

# Register your models here.
from .models import Satellite, LaunchCountry, SatelliteHistory

admin.site.register(Satellite)
admin.site.register(LaunchCountry)
admin.site.register(SatelliteHistory)

