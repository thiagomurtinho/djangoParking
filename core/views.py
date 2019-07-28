from django.shortcuts import render
from .models import (
    Person,
    Vehicle,
    RotaryMotion,
    Monthly,
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

def monthly(request):
    monthly  = Monthly.objects.all()
    
    context = {
        'monthly': monthly,
    }

    return render(request, 'core/monthlyList.html', context)

