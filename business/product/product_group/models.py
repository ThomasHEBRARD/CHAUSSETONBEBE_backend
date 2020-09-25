from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from business.shared.models import BaseModel


class ProductGroup(MPTTModel, BaseModel):
    parent = TreeForeignKey(
        "self", on_delete=models.DO_NOTHING, null=True, blank=True, related_name="children"
    )
