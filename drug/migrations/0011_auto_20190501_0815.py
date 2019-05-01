# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-05-01 00:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drug', '0010_drug_important_is_ordered'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drug_order',
            old_name='date',
            new_name='ordered_date',
        ),
        migrations.RemoveField(
            model_name='drug_order',
            name='drug_order_status',
        ),
        migrations.AddField(
            model_name='drug_order',
            name='name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='drug.Drug_detail'),
        ),
        migrations.AlterField(
            model_name='drug_important',
            name='shirheg',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='drug_order',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]
