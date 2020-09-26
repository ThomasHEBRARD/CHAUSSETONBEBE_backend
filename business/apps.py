from django.apps import AppConfig


class BusinessConfig(AppConfig):
    name = "business"

    def ready(self):
        from business.product.product_group.models import ProductGroup
        from business.product.product.models import Product
