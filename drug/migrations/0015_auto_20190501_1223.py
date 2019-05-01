# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-05-01 04:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_remove_degree_date'),
        ('drug', '0014_auto_20190501_1216'),
    ]

    operations = [
        migrations.CreateModel(
            name='costumer_review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.IntegerField(default=1)),
                ('costumer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Costumer')),
            ],
        ),
        migrations.CreateModel(
            name='doctor_review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.IntegerField(default=1)),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Worker')),
            ],
        ),
        migrations.RemoveField(
            model_name='emchilgee',
            name='cos_review',
        ),
        migrations.RemoveField(
            model_name='emchilgee',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='emchilgee',
            name='doctor_review',
        ),
        migrations.AddField(
            model_name='doctor_review',
            name='emchilgee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='drug.Emchilgee'),
        ),
        migrations.AddField(
            model_name='costumer_review',
            name='emchilgee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='drug.Emchilgee'),
        ),
    ]
