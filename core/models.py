from django.db import models


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
    brand = models.ForeignKey(Brand, related_name='brand', on_delete=models.CASCADE)
    owner = models.ForeignKey(Person, related_name='person', on_delete=models.CASCADE)
    board = models.CharField(max_length=50)
    color = models.CharField(max_length=15)
    comments= models.TextField()

    def __str__(self):
        return self.brand.name + ' - ' + self.board

    def __unicode__(self):
        return self.board

class Parameters(models.Model):
    priceHour   = models.DecimalField(max_digits=3, decimal_places=2)
    monthHour   = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return 'Parameters'

    def __unicode__(self):
        return 'Parameters'