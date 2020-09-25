from django.db import migrations
from utils.migration_helper import create_if_non_existent

ROOT_PRODUCT_GROUP_PARAMS = {
    "parent": None,
    "name": "ROOT",
    "code": "ROOT",
    "description": "The root of product groups",
    "level": 0,
    "lft": 0,
    "rght": 0,
    "tree_id": 0,
}


def forwards_func(apps, schema_editor):
    create_if_non_existent(apps, "business", "ProductGroup", ROOT_PRODUCT_GROUP_PARAMS)


def reverse_func(apps, schema_editor):
    ProductGroup = apps.get_model("business", "ProductGroup")
    ProductGroup.objects.filter(code="ROOT").delete()


class Migration(migrations.Migration):

    initial = False

    dependencies = [("business", "0001_product_and_productgroup")]

    operations = [migrations.RunPython(forwards_func, reverse_func)]
