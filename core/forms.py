from django.forms import ModelForm
from .models import (
    Person,
    Vehicle,
    RotaryMotion,
    Monthly,
    RotaryMonthly,
    )


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'


class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'


class RotaryMotionForm(ModelForm):
    class Meta:
        model = RotaryMotion
        fields = '__all__'


class MonthlyForm(ModelForm):
    class Meta:
        model = Monthly
        fields = '__all__'


class RotaryMonthlyForm(ModelForm):
    class Meta:
        model = RotaryMonthly
        fields = '__all__'