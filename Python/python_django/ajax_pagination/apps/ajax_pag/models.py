from __future__ import unicode_literals
from django.db import models
from datetime import date
from django.utils.dateparse import parse_date


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    registered = models.DateField(auto_now = False)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<User: {} |{} {} {} {} {}>".format(self.id, self.first_name, self.last_name, self.email, self.registered, self.created_at)
