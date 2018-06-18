from __future__ import unicode_literals
from django.db import models
import re

# Create your models here.
class CigarManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 2:
            errors['name'] = "Cigar name needs to be at least two characters"
        return errors

class Cigars(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<Cigars: {} |{} {} {}>".format(self.id, self.name, self.price, self.created_at)
    objects = CigarManager()