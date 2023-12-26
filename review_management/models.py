# review_management/models.py

from django.db import models
from user_authentication.models import Customer
from boat_management.models import Boat

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    cust = models.ForeignKey(Customer, on_delete=models.CASCADE)
    boat = models.ForeignKey(Boat, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
