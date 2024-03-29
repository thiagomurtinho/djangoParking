from django.db import models
import math


class Person(models.Model):
    name   = models.CharField(max_length=100)
    adress = models.CharField(max_length=200)
    phone  = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Brand(models.Model):
    name   = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Vehicle(models.Model):
    brand    = models.ForeignKey(Brand, related_name='brand', on_delete=models.CASCADE)
    owner    = models.ForeignKey(Person, related_name='person', on_delete=models.CASCADE)
    board    = models.CharField(max_length=50)
    color    = models.CharField(max_length=15)
    comments = models.TextField()

    def __str__(self):
        return self.brand.name + ' - ' + self.board

    def __unicode__(self):
        return self.board

class Parameters(models.Model):
    priceHour   = models.DecimalField(max_digits=5, decimal_places=2)
    monthHour   = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return 'Parameters'

    def __unicode__(self):
        return 'Parameters'

class RotaryMotion(models.Model):
    checkin   = models.DateTimeField(auto_now=False)
    checkout  = models.DateTimeField(auto_now=False, null=True, blank=True)
    priceHour = models.DecimalField(max_digits=5, decimal_places=2)
    vehicle   = models.ForeignKey(Vehicle, related_name='vehicleRotary', on_delete=models.CASCADE)
    paid      = models.BooleanField(default=False)

    def totalHours(self):
        print(type(self.checkout))
        if self.checkout == None:
            return 'Not finished'
        return math.ceil((self.checkout - self.checkin).total_seconds() / 3600)

    def payable(self):
        if self.checkout == None:
            return 'Not finished'
        return 'R$' + str(self.priceHour * self.totalHours())

    def __str__(self):
        return self.vehicle.board 

    def __unicode__(self):
        return self.vehicle.board

class Monthly(models.Model):
    vehicle    = models.ForeignKey(Vehicle, related_name='vehicleMounth', on_delete=models.CASCADE)
    checkin    = models.DateField()
    priceMouth = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.vehicle) + ' - ' + str(self.checkin)

    def __unicode__(self):
        return self.vehicle.board

class RotaryMonthly(models.Model):
    monthly = models.ForeignKey(Monthly, related_name='monthly', on_delete=models.CASCADE)
    payDay = models.DateField()
    totalPaid = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.monthly) + ' - ' + str(self.totalPaid)

    def __unicode__(self):
        return self.totalPaid