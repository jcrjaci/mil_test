"""Trip's app models."""

import uuid

from django.db import models
from django.contrib.postgres.fields import ArrayField
from .vehicles import Vehicle


class Trip(models.Model):
    """Model representing a vehicle's trip."""

    TRIP_RUNNING = 'R'
    TRIP_FINISHED = 'F'
    TRIP_CHOICES = (
        (TRIP_RUNNING, 'Running'),
        (TRIP_FINISHED, 'Finished'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vehicle = models.ForeignKey(Vehicle)
    coordinates_json = ArrayField(models.TextField())
    alerts_json = ArrayField(models.TextField())
    status = models.CharField(max_length=1,
                              choices=TRIP_CHOICES,
                              default=TRIP_RUNNING)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True)
    duration = models.IntegerField(null=True)  # in minutes
    length = models.FloatField(null=True)  # in meters
    end_fuel = models.IntegerField(null=True)
    consumed_fuel = models.FloatField(null=True)  # in litres

    def __str__(self):
        """String representation of the object."""

        return "{0}, {1} - {2}".format(self.vehicle.tracker_id, self.start_date, self.end_date)

    class Meta:
        db_table = 'trips_trip'
        app_label = 'milefrienddb'
