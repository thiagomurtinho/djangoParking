from django.shortcuts import render, redirect
from .models import (
    Person,
    Vehicle,
    RotaryMotion,
    Monthly,
    RotaryMonthly,
    )
from .forms import (
    PersonForm,
    VehicleForm,
    RotaryMotionForm,
)


def home(request):
    context ={
        'messenger': 'Hello word',
    }

    return render(request, 'core/index.html', context)

#Person Viwes
def personList(request):
    people  = Person.objects.all()
    form    = PersonForm()
    
    context = {
        'people': people,
        'form'  : form,
    }

    return render(request, 'core/personList.html', context)

def newPerson(request):
    form = PersonForm(request.POST or None)
    if form.is_valid():
        form.save()

    return redirect('core_persons_list')

#Vehicle Viwes
def vehicleList(request):
    vehicles = Vehicle.objects.all()
    form     = VehicleForm()

    context  = {
        'vehicles': vehicles,
        'form'    : form,
    }

    return render(request, 'core/vehicleList.html', context)


def newVehicle(request):
    form = VehicleForm(request.POST or None)
    if form.is_valid():
        form.save()

    return redirect('core_vehicles_list')

#Rotary Motion Viwes
def rotaryMotion(request):
    rotaryMotions = RotaryMotion.objects.all()
    form          = RotaryMotionForm()

    context       = {
        'rotaryMotions': rotaryMotions,
        'form'         : form,
    }

    return render(request, 'core/rotaryMotionList.html', context)


def newRotaryMotion(request):
    form = RotaryMotionForm(request.POST or None)
    if form.is_valid():
        form.save()

    return redirect('core_rotaryMotion_list')

def monthly(request):
    monthly  = Monthly.objects.all()
    
    context = {
        'monthly': monthly,
    }

    return render(request, 'core/monthlyList.html', context)

def rotaryMonthly(request):
    rotaryMonthly  = RotaryMonthly.objects.all()
    
    context = {
        'rotaryMonthly': rotaryMonthly,
    }

    return render(request, 'core/rotaryMonthlyList.html', context)

