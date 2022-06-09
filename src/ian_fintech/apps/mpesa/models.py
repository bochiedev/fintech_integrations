from django.db import models
from django.utils import timezone

# Create your models here.

class Transaction(models.Model):
    id = models.BigAutoField()
    timestamp = models.DateTimeField(default=timezone.now())
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
