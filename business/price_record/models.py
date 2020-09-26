from business.shared.models import BaseModel
from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone
from business.product.product.models import Product


class PriceRecordStatusChoice(models.TextChoices):
    success = "SUCCESS"
    pending = "PENDING"
    failure = "FAILURE"
    canceled = "CANCELED"


class PriceRecord(BaseModel):
    price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True, validators=[MinValueValidator(0)]
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="price_records")
    valid_since = models.DateTimeField(null=True, blank=False, default=timezone.now)
    valid_to = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        max_length=64,
        choices=PriceRecordStatusChoice.choices,
        default=PriceRecordStatusChoice.pending,
        null=False,
    )
    # TODO: add users
