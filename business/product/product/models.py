from django.db import models
from business.shared.models import BaseModel
from business.product.product_group.models import ProductGroup
from django.core.validators import MinValueValidator


class Product(BaseModel):
    price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True, validators=[MinValueValidator(0)]
    )
    overriden_price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True, validators=[MinValueValidator(0)]
    )
    shipping_price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True, validators=[MinValueValidator(0)]
    )
    stock = models.IntegerField(blank=True, null=True)
    is_linked = models.BooleanField(default=True)
    image = models.ImageField(null=True)
    group = models.ForeignKey(
        ProductGroup, related_name="entries", on_delete=models.DO_NOTHING, blank=False, null=False
    )
