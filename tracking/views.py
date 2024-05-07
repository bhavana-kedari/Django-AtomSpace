from django.shortcuts import render

# Create your views here.
from .models import Satellite, LaunchCountry

def index(request):
    return render(request, 'index.html')

def satellite_display(request):
    satellites = Satellite.objects.all()
    return render(request, 'satellite.html', {'satellites': satellites})

def launch_display(request):
    launch_countries = LaunchCountry.objects.all()
    return render(request, 'launchCountry.html', {'launch_countries': launch_countries})

from django.shortcuts import render
from .models import Satellite, SatelliteHistory

from django.shortcuts import render, get_object_or_404
from .models import Satellite, SatelliteHistory

def satellite_list(request):
    satellites = Satellite.objects.all()
    return render(request, 'satellite.html', {'satellites': satellites})

def satellite_history(request, satellite_id):
    satellite = get_object_or_404(Satellite, pk=satellite_id)
    history_entries = SatelliteHistory.objects.filter(satellite=satellite)
    return render(request, 'satellite_history.html', {'satellite': satellite, 'history_entries': history_entries})

