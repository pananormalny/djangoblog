# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-15 19:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eblog', '0003_auto_20150506_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
