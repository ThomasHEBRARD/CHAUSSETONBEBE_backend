# Generated by Django 3.0.6 on 2020-07-05 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0004_auto_20200705_1033'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='businessmodel',
            options={'ordering': ['id']},
        ),
    ]