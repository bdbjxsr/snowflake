# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-16 02:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('framework', '0002_auto_20171114_20341111111111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='framework.Department'),
        ),
    ]
