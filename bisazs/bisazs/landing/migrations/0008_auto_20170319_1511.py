# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-19 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0007_auto_20170319_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_3',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='interval_3',
            field=models.TimeField(null=True),
        ),
    ]