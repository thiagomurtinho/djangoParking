from django.shortcuts import render
from .models import Person

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
