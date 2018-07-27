from __future__ import unicode_literals
from django.db import models
import bcrypt
import re
from django.db.models import Count

EMAIL_REGEX = re.compile('^[_a-z0-9-]+(.[_a-z0-9-]+)@[a-z0-9-]+(.[a-z0-9-]+)(.[a-z]{2,4})$')
PASSWORD_REGEX = re.compile('^[A-Za-z0-9#!*@$%^&.()\-_]{8,32}$')
USERNAME_REGEX = re.compile('^[A-Za-z0-9#!*@$%^&.()\-_]{5,32}$')
SLOGAN_REGEX = re.compile('^[A-Za-z0-9#!*@$%^&.,()\- _]{5,160}$')
TEAMNAME_REGEX = re.compile('^[A-Za-z0-9#!*@$%^&.()\- _]{5,32}$')


class UserManager(models.Manager):
    def login_validator(self, postData):
        errors = {}
        if not postData['username']:
            errors['username'] = "Cannot submit blank data!"
            print(errors)
            print("user submited blank data")
            return errors
        if not postData['password']:
            errors['password'] = "Cannot submit blank data!"
            print("user submited blank data")
            return errors
        if not User.objects.filter(username= postData['username']):
            errors['username'] = 'Account does not exist.'
            return errors
        if User.objects.filter(username = postData['username']):
            user = User.objects.get(username = postData['username'])
        if postData['password'] == user.password:
            return errors
        else:
            if re.match(user.username, postData['username']):
                if not postData['password'] == user.password:
                    errors['password'] = "Password is incorrect."
            else:
                errors['username'] = "Invalid Username."

    def update_validator(self, postData, username):
        errors = {}
        if not postData['email']:
            errors['blank'] = 'No field can be left blank, please fill in all fields, then submit.'
        if not postData['slogan']:
            errors['blank'] = 'No field can be left blank, please fill in all fields, then submit.'
        if not postData['team_name']:
            errors['blank'] = 'No field can be left blank, please fill in all fields, then submit.'
        if not postData['username']:
            errors['blank'] = 'No field can be left blank, please fill in all fields, then submit.'
        if User.objects.filter(email=postData['email']).exclude(username=username).exists():
            errors['update email unique'] = "This email address has already been registered"
        if User.objects.filter(username=postData['username']).exclude(username=username).exists():
            errors['update username unique'] = "This username has already been registered"
        if not re.match(SLOGAN_REGEX, postData['slogan']):
            errors['password'] = 'Slogan must be between 5 and 160 characters, and can contain letters, numbers, and the following split characters: #!*@$%^&.,()\- _.'
        if not re.match(TEAMNAME_REGEX, postData['team_name']):
            errors['team_name'] = 'Team name must be between 5 and 32 characters, and can contain letters, numbers, and the following split characters: #!*@$%^&.()\- _.'
        if not re.match(EMAIL_REGEX, postData['email']):
            errors['email'] = 'Email is not valid.'
        if not re.match(USERNAME_REGEX, postData['username']):
            errors['username'] = 'Username must between 5 and 32 characters, and can only include letters and numbers.'
        return errors

    def message_validator(self, postData, username):
        errors = {}
        print("in validator")
        if not postData['message_text']:
            errors['blank'] = 'Message cannot be blank.'
            return errors
        # if not postData['comment']:
        #     errors['blank'] = 'Comment cannot be blank.'
        if not re.match(SLOGAN_REGEX, postData['message_text']):
            errors['message'] = 'Message must be between 5 and 160 characters, and can contain letters, numbers, and the following split characters: #!*@$%^&.,()\- _.'
            return errors
        return errors

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=32)
    team_name = models.CharField(max_length=32)
    slogan = models.TextField(max_length=160)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now= True)
    updated_at = models.DateTimeField(auto_now= True)
    objects = UserManager()
    def __repr__(self):
        return "<User: {}|{} {} {} {} {} {}>".format(self.id, self.name, self.username, self.team_name, self.slogan, self.email, self.password)

class Player(models.Model):
    name = models.CharField(max_length=255)
    years = models.IntegerField()
    salary = models.IntegerField()
    created_at = models.DateTimeField(auto_now= True)
    updated_at = models.DateTimeField(auto_now= True)
    has_manager = models.ForeignKey(User, related_name='has_player', on_delete=models.CASCADE)
    objects = UserManager()
    def __repr__(self):
        return "<Player: {}|{}>".format(self.id, self.text)

class Messaging(models.Model):
    text = models.TextField(max_length=1000)
    user = models.ForeignKey(User, related_name="has_message", blank=True)
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<Message: {} | {} {}>".format(self.id, self.text, self.created_at)
    objects = UserManager()

# class Comment(models.Model):
#     text = models.TextField(max_length=1000)
#     user = models.ForeignKey(User, related_name="has_comments", blank=True)
#     message = models.ForeignKey(Message, related_name="has_comments", blank=True)
#     created_at = models.DateTimeField(auto_now = True)
#     updated_at = models.DateTimeField(auto_now = True)
#     def __repr__(self):
#         return "<Comment: {} | {} {}>".format(self.id, self.message, self.created_at)
#     objects = UserManager()
