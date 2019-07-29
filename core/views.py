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
    MonthlyForm,
    RotaryMonthlyForm,
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


def updatePerson(request, id):
    person = Person.objects.get(id=id)
    form   = PersonForm(request.POST or None, instance=person)
    data   = {
        'person': person,
        'form'  : form,
    }
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_persons_list')
    else:
        return render(request, 'core/personUpdate.html', data)

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

#Monthly Viwes
def monthly(request):
    monthly = Monthly.objects.all()
    form    = MonthlyForm()

    context = {
        'monthly': monthly,
        'form'   : form
    }

    return render(request, 'core/monthlyList.html', context)


def newMonthly(request):
    form = MonthlyForm(request.POST or None)
    if form.is_valid():
        form.save()

    return redirect('core_monthly_list')

#Rotary Monthly Views
def rotaryMonthly(request):
    rotaryMonthly = RotaryMonthly.objects.all()
    form          = RotaryMonthlyForm()
    
    context       = {
        'rotaryMonthly': rotaryMonthly,
        'form'         : form,
    }

    return render(request, 'core/rotaryMonthlyList.html', context)


def newRotaryMonthly(request):
    form = RotaryMonthlyForm(request.POST or None)
    if form.is_valid():
        form.save()

    return redirect('core_rotaryMonthly_list')

