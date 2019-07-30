from django.urls import path
from .views import (
    home, 
    personList,
    newPerson,
    updatePerson,
    vehicleList,
    newVehicle,
    updateVehicle,
    rotaryMotion,
    newRotaryMotion,
    updateRotaryMotion,
    monthly,
    rotaryMonthly,
    newMonthly,
    newRotaryMonthly,
    )


urlpatterns = [
    path('', home, name='core_home'),
    #Person URLs
    path('person_list/', personList, name='core_persons_list'),
    path('person_new/', newPerson, name='core_persons_new'),
    path('person_new/<id>/', updatePerson, name='core_persons_update'),
    #Vehicle URLs
    path('vehicle_list/', vehicleList, name='core_vehicles_list'),
    path('vehicle_new/', newVehicle, name='core_vehicles_new'),
    path('vehicle_update/<id>/', updateVehicle, name='core_vehicle_update'),
    #Rotary Motion URLs
    path('rotaryMotion_list/', rotaryMotion, name='core_rotaryMotion_list'),
    path('rotaryMotion_new/', newRotaryMotion, name='core_rotaryMotion_new'),
    path('rotaryMotion_update/<id>/', updateRotaryMotion, name='core_rotaryMotion_update'),
    #Monthly URLs
    path('monthly_list/', monthly, name='core_monthly_list'),
    path('monthly_new/', newMonthly, name='core_monthly_new'),
    #Rotary Monthly URLs
    path('rotaryMonthly_list/', rotaryMonthly, name='core_rotaryMonthly_list'),
    path('rotaryMonthly_new/', newRotaryMonthly, name='core_rotaryMonthly_new'),
]
