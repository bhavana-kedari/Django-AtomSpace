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
