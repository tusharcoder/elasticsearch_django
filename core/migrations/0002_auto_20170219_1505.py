# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-19 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('downloadable_product', 'DOWNLOADABLE PRODUCT'), ('shipped_product', 'SHIPPED PRODUCT')], default='downloadable_field', max_length=50),
        ),
    ]