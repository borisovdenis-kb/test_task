# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-07 06:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_task_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='offers',
            options={'permissions': (('view_offers', 'Can see one or several offers.'),)},
        ),
    ]
