from django.db import models

# Create your models here.

class B2CTransaction(models.Model):
    originator_conversation_id = models.CharField(max_length=100)
    initiator_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    party_a = models.CharField(max_length=100)
    party_b = models.CharField(max_length=100)
    remarks = models.TextField()
    occasion = models.CharField(max_length=100, null=True, blank=True)