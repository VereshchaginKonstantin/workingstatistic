# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 12:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0007_auto_20171028_2240'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lightning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.BigIntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bot.groupUser')),
            ],
        ),
    ]