from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    # path('satellites/', views.satellite_display, name='satellite'),
    path('launch-countries/', views.launch_display, name='launchCountry'),
    path('satellites/', views.satellite_list, name='satellite_list'),
    path('satellite/<int:satellite_id>/', views.satellite_history, name='satellite_history'),
]