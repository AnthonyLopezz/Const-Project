# Generated by Django 3.1.7 on 2021-06-01 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StoreApp', '0002_remove_product_availability'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='type',
            new_name='classification',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='size',
            new_name='platform',
        ),
    ]
