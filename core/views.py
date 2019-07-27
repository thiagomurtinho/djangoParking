from django.shortcuts import render
from .models import (
    Person,
    Vehicle,
    RotaryMotion
    )


def home(request):
    context ={
        'messenger': 'Hello word',
    }

    return render(request, 'core/index.html', context)


def personList(request):
    people  = Person.objects.all()
    
    context = {
        'people': people,
    }

    return render(request, 'core/personList.html', context)


def vehicleList(request):
    vehicles  = Vehicle.objects.all()
    
    context = {
        'vehicles': vehicles,
    }

    return render(request, 'core/vehicleList.html', context)


def rotaryMotion(request):
    rotaryMotions  = RotaryMotion.objects.all()
    
    context = {
        'rotaryMotions': rotaryMotions,
    }

    return render(request, 'core/rotaryMotionList.html', context)

