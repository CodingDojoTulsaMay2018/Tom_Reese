from __future__ import unicode_literals
from django.db import models

class Note(models.Model):
      text = models.TextField(max_length=255)
      created_at = models.DateTimeField(auto_now = True)
      updated_at = models.DateTimeField(auto_now = True)