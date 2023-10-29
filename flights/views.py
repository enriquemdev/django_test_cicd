from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Flight, Passenger, Airport

# Create your views here.
def index(request):
    context = {
        "flights": Flight.objects.all(),
        "airports": Airport.objects.all()
    }
    return render(request, "index.html", context)

def save(request):
    if request.method == "POST":
        origin_instance = Airport.objects.get(pk=request.POST.get('origin'))
        destination_instance = Airport.objects.get(pk=request.POST.get('destination'))
        duration = request.POST.get('duration')
        
        new_flight = Flight(
            origin=origin_instance,
            destination=destination_instance,
            duration=duration
        )
        
        new_flight.save()
        return redirect("index")
