from django.db import models

# Create your models here.

class AddressBook(models.Model):
    long_position   = models.DecimalField (max_digits=8, decimal_places=3)
    lat_position   = models.DecimalField (max_digits=8, decimal_places=3)
