from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('satellites/', views.satellite_display, name='satellite'),
    path('launch-countries/', views.launch_display, name='launchCountry'),
]