from django.shortcuts import render

def home(request):
    context ={
        'messenger': 'Hello word',
    }

    return render(request, 'core/index.html', context)
