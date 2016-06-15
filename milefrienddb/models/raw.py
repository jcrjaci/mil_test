"""Raw's app models."""

import uuid

from django.db import models


class Log(models.Model):
    """Model that saves raw packets coming from the devices."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=16)
    tracker_id = models.CharField(max_length=64)
    packet_hex = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String representation of the object."""
        return "{0}: {1}, {2}".format(self.type, self.tracker_id, self.date_created)
    
    class Meta:
        db_table = 'raw_log'
        app_label = 'milefrienddb'
