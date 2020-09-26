from django.db import models
from business.product.product.models import Product
from busness.shared.models import BaseModel


class PreOrder(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, related_name="pre_orders")

    # TODO: add users
