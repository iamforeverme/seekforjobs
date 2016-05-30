# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-23 14:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='jobModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('onlineDate', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('location', models.CharField(blank=True, default='', max_length=100)),
                ('workType', models.CharField(blank=True, default='', max_length=100)),
                ('salary', models.CharField(blank=True, default='', max_length=100)),
                ('tags', models.CharField(blank=True, default='', max_length=100)),
            ],
            options={
                'ordering': ('onlineDate',),
            },
        ),
    ]
