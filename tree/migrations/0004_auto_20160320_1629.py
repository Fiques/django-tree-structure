# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-20 16:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0003_auto_20160320_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='earnings',
            field=models.IntegerField(blank=True),
        ),
    ]
