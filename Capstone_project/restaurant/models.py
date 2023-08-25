from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=225)
    no_of_guests = models.IntegerField()
    bookingdate = models.DateTimeField()

class Menu(models.Model):
    title = models.CharField(max_length=225)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()