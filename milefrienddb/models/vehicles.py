"""Vehicle's app models."""

import uuid
from django.db import models
from .clients import Client


class Vehicle(models.Model):
    """Model representing a vehicle."""

    road_worthiness_path = 'vehicles/certs/road_worthiness'
    ownership_path = 'vehicles/certs/ownership'
    photo_path = 'vehicles/photos'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client = models.ForeignKey(Client, null=True)

    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    year = models.IntegerField(null=True)
    license_plate_number = models.CharField(max_length=20)
    tracker_id = models.CharField(max_length=64)
    car_value = models.FloatField(null=True)
    cert_road_worthiness = models.FileField(upload_to=road_worthiness_path)
    cert_ownership = models.FileField(upload_to=ownership_path)
    policy_number = models.CharField(max_length=255)
    photo = models.FileField(upload_to=photo_path)
    date_insurance = models.DateTimeField(null=True)
    premium_paid = models.FloatField(null=True)
    bonus_paid = models.FloatField(null=True)
    net_premium = models.FloatField(null=True)
    driven_meters = models.IntegerField(default=0)
    driven_minutes = models.IntegerField(default=0)
    total_fuel_consumption = models.FloatField(null=True, blank=True)
    car_health = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String representation of the object."""
        return "{0}, {1}, {2}".format(self.make, self.model, self.license_plate_number)

    class Meta:
        db_table = 'vehicles_vehicle'
        app_label = 'milefrienddb'
