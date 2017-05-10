# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-08 01:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0005_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockExchange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=5, unique=True)),
                ('name', models.CharField(max_length=120, unique=True)),
            ],
        ),
    ]