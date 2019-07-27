from django.contrib import admin
from .models import (
    Brand, 
    Person, 
    Vehicle, 
    Parameters,
    RotaryMotion,
    Monthly,
    )

class RotaryMotionAdmin(admin.ModelAdmin):
    list_display = (
        'vehicle',
        'checkin',
        'checkout',
        'totalHours',
        'payable',
        'paid',
        )
admin.site.register(RotaryMotion, RotaryMotionAdmin)


admin.site.register(Brand)
admin.site.register(Person)
admin.site.register(Vehicle)
admin.site.register(Parameters)
admin.site.register(Monthly)