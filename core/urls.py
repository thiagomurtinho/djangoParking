from django.urls import path
from .views import (
    home, 
    personList,
    newPerson,  
    vehicleList,
    newVehicle,
    rotaryMotion,
    monthly,
    rotaryMonthly,
    )


urlpatterns = [
    path('', home, name='core_home'),
    #Person URLs
    path('person_list/', personList, name='core_persons_list'),
    path('person_new/', newPerson, name='core_persons_new'),
    #Vehicle URLs
    path('vehicle_list/', vehicleList, name='core_vehicles_list'),
    path('vehicle_new/', newVehicle, name='core_vehicles_new'),
    path('rotaryMotion_list/', rotaryMotion, name='core_rotaryMotion_list'),
    path('monthly_list/', monthly, name='core_monthly_list'),
    path('rotaryMonthly_list/', rotaryMonthly, name='core_rotaryMonthly_list'),
]
