# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-15 14:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('csvimport', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('code', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('latitude', models.FloatField(null=True, default=0)),
                ('longitude', models.FloatField(null=True, default=0)),
                ('alias', models.CharField(max_length=255, null=True)),
            ],
            options={
                'managed': True,
                'db_table': '"csvtests_country"',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TYPE', models.PositiveIntegerField(default=0)),
                ('code_share', models.CharField(help_text='Cross-organization item code', max_length=32)),
                ('code_org', models.CharField(help_text='Organization-specfific item code', max_length=32)),
                ('description', models.TextField(null=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('status', models.CharField(max_length=10, null=True)),
                ('date', models.DateField(auto_now=True, null=True)),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='csvimport.Country')),
            ],
            options={
                'managed': True,
                'db_table': 'csvtests_item',
            },
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'managed': True,
                'db_table': 'csvtests_organisation',
            },
        ),
        migrations.CreateModel(
            name='UnitOfMeasure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
            options={
                'managed': True,
                'db_table': 'csvtests_unitofmeasure',
            },
        ),
        migrations.AddField(
            model_name='item',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='csvimport.Organisation'),
        ),
        migrations.AddField(
            model_name='item',
            name='uom',
            field=models.ForeignKey(help_text='Unit of Measure', on_delete=django.db.models.deletion.CASCADE, to='csvimport.UnitOfMeasure'),
        ),
    ]
