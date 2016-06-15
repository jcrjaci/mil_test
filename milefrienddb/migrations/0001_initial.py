# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.postgres.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('user_uuid', models.UUIDField(default=uuid.uuid4, unique=True, editable=False)),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('email', models.EmailField(unique=True, max_length=254, verbose_name='Email address')),
                ('gender', models.CharField(default='M', choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('confirmed_email', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff status')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('date_joined', models.DateTimeField(verbose_name='date joined', auto_now_add=True)),
                ('activation_key', models.UUIDField(default=uuid.uuid4, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, editable=False, default=uuid.uuid4)),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('street', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=16)),
                ('email', models.CharField(max_length=64)),
                ('driver_license', models.FileField(upload_to='clients/driver_license', blank=True)),
                ('photo', models.FileField(upload_to='clients/photos')),
                ('bank_name', models.CharField(max_length=32)),
                ('bank_account_number', models.CharField(max_length=255)),
                ('insured_score', models.FloatField(default=0)),
                ('is_company', models.BooleanField(default=False)),
                ('certificate_incorporation', models.FileField(upload_to='clients/certificate_incorporation', blank=True)),
                ('utility_bill', models.FileField(upload_to='clients/utility_bill', blank=True)),
            ],
            options={
                'db_table': 'clients_client',
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, editable=False, default=uuid.uuid4)),
                ('type', models.CharField(max_length=16)),
                ('tracker_id', models.CharField(max_length=64)),
                ('packet_hex', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'raw_log',
            },
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, editable=False, default=uuid.uuid4)),
                ('coordinates_json', django.contrib.postgres.fields.ArrayField(size=None, base_field=models.TextField())),
                ('alerts_json', django.contrib.postgres.fields.ArrayField(size=None, base_field=models.TextField())),
                ('status', models.CharField(default='R', choices=[('R', 'Running'), ('F', 'Finished')], max_length=1)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField(null=True)),
                ('duration', models.IntegerField(null=True)),
                ('length', models.FloatField(null=True)),
                ('end_fuel', models.IntegerField(null=True)),
                ('consumed_fuel', models.FloatField(null=True)),
            ],
            options={
                'db_table': 'trips_trip',
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, editable=False, default=uuid.uuid4)),
                ('make', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=20)),
                ('year', models.IntegerField(null=True)),
                ('license_plate_number', models.CharField(max_length=20)),
                ('tracker_id', models.CharField(max_length=64)),
                ('car_value', models.FloatField(null=True)),
                ('cert_road_worthiness', models.FileField(upload_to='vehicles/certs/road_worthiness')),
                ('cert_ownership', models.FileField(upload_to='vehicles/certs/ownership')),
                ('policy_number', models.CharField(max_length=255)),
                ('photo', models.FileField(upload_to='vehicles/photos')),
                ('date_insurance', models.DateTimeField(null=True)),
                ('premium_paid', models.FloatField(null=True)),
                ('bonus_paid', models.FloatField(null=True)),
                ('net_premium', models.FloatField(null=True)),
                ('driven_meters', models.IntegerField(default=0)),
                ('driven_minutes', models.IntegerField(default=0)),
                ('total_fuel_consumption', models.FloatField(blank=True, null=True)),
                ('car_health', models.TextField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(to='milefrienddb.Client', null=True)),
            ],
            options={
                'db_table': 'vehicles_vehicle',
            },
        ),
        migrations.AddField(
            model_name='trip',
            name='vehicle',
            field=models.ForeignKey(to='milefrienddb.Vehicle'),
        ),
    ]
