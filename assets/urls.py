from django.urls import path
from . import views


app_name = 'assets'
urlpatterns = [
    path('vehicles/', views.vehicles, name="vehicles"),
    path('trollies/', views.trollies, name="trollies"),
    path('equipments/', views.equipments, name="equipments"),
    path('tools/', views.tools, name="tools"),
]
