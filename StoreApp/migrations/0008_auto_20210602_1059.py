# Generated by Django 3.1.7 on 2021-06-02 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StoreApp', '0007_auto_20210602_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='StoreApp.categoryprod'),
        ),
    ]
