# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-05-27 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drug', '0025_days_of_emchilgee_drug'),
    ]

    operations = [
        migrations.AddField(
            model_name='days_of_emchilgee',
            name='category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]