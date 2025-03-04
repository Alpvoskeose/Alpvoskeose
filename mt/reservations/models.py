from django.db import models
from customers.models import Customer
from tables.models import Table

class ReservationStatus(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateTimeField()
    status = models.ForeignKey(ReservationStatus, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.customer} - {self.table} on {self.date}"
