from django.urls import path
from .views import (
    home, 
    personList,  
    vehicleList,
    rotaryMotion,
    monthly,
    )


urlpatterns = [
    path('', home, name='core_home'),
    path('person_list/', personList, name='core_persons_list'),
    path('vehicle_list/', vehicleList, name='core_vehicles_list'),
    path('rotaryMotion_list/', rotaryMotion, name='core_rotaryMotion_list'),
    path('monthly_list/', monthly, name='core_monthly_list'),
]