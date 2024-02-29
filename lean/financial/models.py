from django.db import models

# Create your models here.

class B2BTransaction(models.Model):
    initiator = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    party_a = models.CharField(max_length=100)
    party_b = models.CharField(max_length=100)
    # Add other fields as necessary