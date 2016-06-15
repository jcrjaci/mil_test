"""Clients's app models."""

import uuid

from django.db import models


class Client(models.Model):
    """Model representing a client."""

    DRIVER_LICENSE_PATH = 'clients/driver_license'
    PHOTO_PATH = 'clients/photos'
    CERT_INCORPORATION_PATH = 'clients/certificate_incorporation'
    UTILITY_BILL_PATH = 'clients/utility_bill'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    phone = models.CharField(max_length=16)
    email = models.CharField(max_length=64)
    driver_license = models.FileField(upload_to=DRIVER_LICENSE_PATH, blank=True)
    photo = models.FileField(upload_to=PHOTO_PATH)
    bank_name = models.CharField(max_length=32)
    bank_account_number = models.CharField(max_length=255)
    insured_score = models.FloatField(default=0)
    is_company = models.BooleanField(default=False)
    certificate_incorporation = models.FileField(upload_to=CERT_INCORPORATION_PATH, blank=True)
    utility_bill = models.FileField(upload_to=UTILITY_BILL_PATH, blank=True)

    def __str__(self):
        """String representation of the object."""
        return "{0}, {1} {2}".format(self.id, self.first_name, self.last_name)

    class Meta:
        db_table = 'clients_client'
        app_label = 'milefrienddb'
