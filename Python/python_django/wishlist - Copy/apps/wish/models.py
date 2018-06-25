from __future__ import unicode_literals
from django.db import models
import bcrypt
import re
from django.db.models import Count

EMAIL_REGEX = re.compile('^[_a-z0-9-]+(.[_a-z0-9-]+)@[a-z0-9-]+(.[a-z0-9-]+)(.[a-z]{2,4})$')

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if not postData['name'].isalpha():
            errors['name'] = 'First name only, no special characters or spaces'
        if len(postData['name']) < 3:
            errors['name'] = 'Name should be at least 3 characters.'
        if not postData['username'].isalpha():
            errors['username'] = 'Username must only contain non-alpha characters.'
        if len(postData['username']) < 3:
            errors['username'] = 'Username should be at least 3 characters.'
        if User.objects.filter(username = postData['username']):
            errors['username'] = 'Username already exits.'
        if len(postData['password']) < 8:
            errors['password'] = 'Password should be at least 8 characters.'
        if postData['password'] != postData['confirm']:
            errors['password'] = 'Passwords do not match.'
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

class WishManager(models.Manager):
    def process_wish(self, postData):
        # wish = Wish.objects.create(wish = postData['wish'], dreamer = User.objects.get(id=user_id))
        errors = {}
        if not postData['wish'].isalpha():
            errors['wish'] = 'No special characters or spaces'
        if len(postData['wish']) < 3:
            errors['wish'] = 'Wish should be at least 3 characters.'
        return errors
        
        # return wish

    # def process_like(self, postData):
    #     this_user = User.objects.get(id = postData['user_id'])
    #     this_wish = Secret.objects.get(id = postData['wish_id'])
    #     this_wish.has_dreamers.add(this_user)
    #     has_dreamers = Wish.objects.annotate(count_likes=Count('has_dreamers'))
    #     return liked_users



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
