# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-10 07:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='theme',
            field=models.CharField(default='Test', max_length=64),
        ),
    ]