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


def updateVehicle(request, id):
    vehicles = Vehicle.objects.get(id=id)
    form   = VehicleForm(request.POST or None, instance=vehicles)
    data   = {
        'vehicles': vehicles,
        'form'  : form,
    }
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_vehicles_list')
    else:
        return render(request, 'core/vehicleUpdate.html', data)

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


def updateRotaryMotion(request, id):
    rotaryMotion = RotaryMotion.objects.get(id=id)
    form         = RotaryMotionForm(request.POST or None, instance=rotaryMotion)
    data         = {
        'rotaryMotion': rotaryMotion,
        'form'        : form,
    }
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_rotaryMotion_list')
    else:
        return render(request, 'core/rotaryMotionUpdate.html', data)


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


def updateMonthly(request, id):
    monthly = Monthly.objects.get(id=id)
    form         = MonthlyForm(request.POST or None, instance=monthly)
    data         = {
        'monthly': monthly,
        'form'        : form,
    }
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_monthly_list')
    else:
        return render(request, 'core/monthlyUpdate.html', data)


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


def updateRotaryMonthly(request, id):
    rotaryMonthly = RotaryMonthly.objects.get(id=id)
    form         = RotaryMonthlyForm(request.POST or None, instance=rotaryMonthly)
    data         = {
        'rotaryMonthly': rotaryMonthly,
        'form'        : form,
    }
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_rotaryMonthly_list')
    else:
        return render(request, 'core/rotaryMonthlyUpdate.html', data)
