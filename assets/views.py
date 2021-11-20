from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def vehicles(request):
    return render (request, 'assets/vehicles.html')

def trollies(request):
    return render (request, 'assets/trollies.html')

def equipments(request):
    return render (request, 'assets/equipments.html')

def tools(request):
    return render (request, 'assets/tools.html')
