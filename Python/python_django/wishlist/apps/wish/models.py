from __future__ import unicode_literals
from django.db import models
from datetime import date
from django.utils.dateparse import parse_date
import bcrypt
import re
from django.db.models import Count

EMAIL_REGEX = re.compile('^[_a-z0-9-]+(.[_a-z0-9-]+)@[a-z0-9-]+(.[a-z0-9-]+)(.[a-z]{2,4})$')
PASSWORD_REGEX = re.compile('^[A-Za-z0-9#!*@$%^&.()\-_]{8,32}$')
USERNAME_REGEX = re.compile('^[A-Za-z0-9-]{3,32}$')

class UserManager(models.Manager):
    def create_validator(self, postData):
        errors = {}
        if not postData['name'].isalpha():
            errors['name'] = 'First name only, no special characters or spaces'
        if len(postData['name']) < 3:
            errors['name'] = 'Name should be at least 3 characters.'
        if not re.match(USERNAME_REGEX, postData['username']):
            errors['username'] = 'Username must between 8 and 32 characters, and can only include letters and numbers.'
        if len(postData['username']) < 3:
            errors['username'] = 'Username should be at least 3 characters.'
        if User.objects.filter(username = postData['username']):
            errors['username'] = 'Username already exits.'
        if len(postData['password']) < 8:
            errors['password'] = 'Password should be at least 8 characters.'
        if len(postData['password']) > 32:
            errors['password'] = 'Password can only be up to 32 characters.'
        if not re.match(PASSWORD_REGEX, postData['password']):
            errors['password'] = 'Password may only include letters, numbers, and the following split characters(#!*@$%^&()\-_).'
        if postData['password'] != postData['confirm']:
            errors['password'] = 'Passwords do not match.'
        x = parse_date(postData['hire'])
        if x > date.today():
            errors['hire'] = 'Date cannot be in the future'
        return errors


class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=200, default="password1")
    datehired = models.DateTimeField(auto_now = True)
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<User: {} |{} {} {} {} {}>".format(self.id, self.name, self.username, self.password, self.datehired, self.created_at)
    objects = UserManager()

WISH_REGEX = re.compile('^[A-Za-z0-9#!*@$%^&.()\-_ ]{2,255}$')

class WishManager(models.Manager):
    def process_wish(self, postData,user_id):
        errors = {}
        if not re.match(WISH_REGEX, postData['wish']):
            errors['wish'] = "2 to 255 characters. May include combos of letters, and the following: numbers (0-9), and the following split characters: #!*@$%^&.()\-_"
            return errors
        else:
            Wish.objects.create(wish = postData['wish'], dreamer=User.objects.get(id=user_id))
        return errors
        

class Wish(models.Model):
    wish = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now= True)
    updated_at = models.DateTimeField(auto_now= True)
    dreamer = models.ForeignKey(User, related_name='has_wish')
    has_dreamers = models.ManyToManyField(User, related_name='has_wishes')
    objects = WishManager()
    def __repr__(self):
        return "<Wish: {}|{}>".format(self.id, self.wish)
    objects = WishManager()
