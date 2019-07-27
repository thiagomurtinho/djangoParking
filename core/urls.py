from django.urls import path
from .views import home, personList


urlpatterns = [
    path('', home, name='core_home'),
    path('person_list/', personList, name='core_persons_list'),
]
