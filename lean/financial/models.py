from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract =True
class B2CTransaction(models.Model):
    originator_conversation_id = models.CharField(max_length=100)
    initiator_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    party_a = models.CharField(max_length=100)
    party_b = models.CharField(max_length=100)
    remarks = models.TextField()
    occasion = models.CharField(max_length=100, null=True, blank=True)


class STKpush(AbstractBaseModel):
    phone_number = models.CharField(max_length=100)
    amount = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    received_at = models.DateTimeField(auto_now_add=True)
    checkout_request_id = models.CharField(max_length=255)
    merchant_request_id = models.CharField(max_length=255)
    mpesa_receipt_no = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.phone_number
    
    class Meta:
        verbose_name = 'Transaction'