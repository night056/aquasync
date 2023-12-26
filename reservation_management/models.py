# reservation_management/models.py

from django.db import models
from user_authentication.models import Customer
from boat_management.models import Boat

class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    cust = models.ForeignKey(Customer, on_delete=models.CASCADE)
    boat = models.ForeignKey(Boat, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    people_count = models.IntegerField()
    status = models.CharField(max_length=20)  # confirmed, pending, canceled
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20)  # pending, completed
