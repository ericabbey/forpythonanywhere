# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-01 12:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20170331_2348'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboard',
            name='level',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='ref_id',
            field=models.CharField(default='1ae8f991ce', max_length=10),
        ),
    ]