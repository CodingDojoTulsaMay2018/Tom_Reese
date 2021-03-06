from __future__ import unicode_literals
from django.db import models
import re

# Create your models here.
class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors['name'] = "Course name needs to be at least five characters"
        if len(postData['desc']) < 15:
            errors['desc'] = "Course description needs to be at least fifteen characters"
        return errors

class Courses(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<Course: {} |{} {} {}>".format(self.id, self.name, self.desc, self.created_at)
    objects = CourseManager()