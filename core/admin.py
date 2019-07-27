from django.contrib import admin
from .models import (
    Brand, 
    Person, 
    Vehicle, 
    Parameters,
    RotaryMotion,
    Monthly,
    RotaryMonthly,
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

class RotaryMonthlyAdmin(admin.ModelAdmin):
    list_display = (
        'monthly',
        'payDay',
        'totalPaid',
        )
admin.site.register(RotaryMonthly, RotaryMonthlyAdmin)


admin.site.register(Brand)
admin.site.register(Person)
admin.site.register(Vehicle)
admin.site.register(Parameters)
admin.site.register(Monthly)