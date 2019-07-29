from django.urls import path
from .views import (
    home, 
    personList,
    newPerson,  
    vehicleList,
    rotaryMotion,
    monthly,
    rotaryMonthly,
    )


urlpatterns = [
    path('', home, name='core_home'),
    path('person_list/', personList, name='core_persons_list'),
    path('person_new/', newPerson, name='core_persons_new'),
    path('vehicle_list/', vehicleList, name='core_vehicles_list'),
    path('rotaryMotion_list/', rotaryMotion, name='core_rotaryMotion_list'),
    path('monthly_list/', monthly, name='core_monthly_list'),
    path('rotaryMonthly_list/', rotaryMonthly, name='core_rotaryMonthly_list'),
]
