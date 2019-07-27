from django.contrib import admin
from .models import (
    Brand, 
    Person, 
    Vehicle, 
    Parameters
    )

admin.site.register(Brand)
admin.site.register(Person)
admin.site.register(Vehicle)
admin.site.register(Parameters)
