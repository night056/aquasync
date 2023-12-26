# boat_management/models.py

from django.db import models
from user_authentication.models import Owner, Customer

class Boat(models.Model):
    reg_no = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    year_of_make = models.IntegerField()
    capacity = models.IntegerField()
    services = models.TextField()
    lifejacket = models.IntegerField()
    fire_extinguisher = models.IntegerField()
    location = models.CharField(max_length=255)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    availability = models.BooleanField()
    active_status = models.BooleanField()
