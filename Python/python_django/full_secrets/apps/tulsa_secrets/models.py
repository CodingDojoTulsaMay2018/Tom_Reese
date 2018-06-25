from __future__ import unicode_literals
from django.db import models
import bcrypt
import re
from django.db.models import Count

EMAIL_REGEX = re.compile('^[_a-z0-9-]+(.[_a-z0-9-]+)@[a-z0-9-]+(.[a-z0-9-]+)(.[a-z]{2,4})$')
PASSWORD_REGEX = re.compile('^(?=.*[#!*@$%^&()\-_])(?=.*[a-z])(?=.*[A-Z]).{8,32}$')


class UserManager(models.Manager):
    def create_validator(self, postData):
        errors = {}
        print("User is in model validations")
        if not postData['first_name'].isalpha():
            errors['first_name'] = 'First name contains non-alpha characters.'
        if len(postData['first_name']) < 2:
            errors['first_name'] = 'First name should be at least 2 characters.'
        if len(postData['last_name']) < 2:
            errors['last_name'] = 'Last name should be at least 2 characters.'
        if not postData['last_name'].isalpha():
            errors['last_name'] = 'Last name contains non-alpha characters.'
        if not re.match(EMAIL_REGEX, postData['email']):
            errors['email'] = 'Email is not valid.'
        if len(postData['password']) < 8:
            errors['password'] = 'Password should be at least 8 characters.'
        if len(postData['password']) > 32:
            errors['password'] = 'Password should not exceed 32 characters.'    
        if not re.match(PASSWORD_REGEX, postData['password']):
            errors['password'] = 'Password must include one capital letter, one number, and the following split characters(#!*@$%^&()\-_).'
        if postData['password'] != postData['confirm']:
            errors['password'] = 'Passwords do not match.'
        if User.objects.filter(email = postData['email']):
            errors['email'] = 'Email already exists.'
        return errors


    def login_validator(self, postData):
        errors = {}
        if User.objects.filter(email = postData['email']):
            user = User.objects.get(email=postData['email'])
        if bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
            return errors
        else:
            if re.match(user.email, postData['email']):
                if not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                    errors['password'] = "Password is incorrect."
            else:
                errors['email'] = "Invalid email address."
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now= True)
    updated_at = models.DateTimeField(auto_now= True)
    objects = UserManager()

    def __repr__(self):
        return "<User: {}|{} {} {} {}>".format(self.id, self.first_name, self.last_name, self.email, self.password)

SECRET_REGEX = re.compile('^(?=.*[!?.-])(?=.*[a-z])(?=.*[A-Z]).{2,200}$')

class SecretManager(models.Manager):
    def process_secret(self, postData, user_id):
        errors = {}
        user = User.objects.get(id=user_id)
        if len(postData['secret']) < 2:
            errors['secret'] = 'Secret was too short'
            return errors
        if len(postData['secret']) > 200:
            errors['secret'] = 'Secret was too long'
            return errors
        print(user.first_name, user.last_name,'is creating secret....')
        errors['secret'] = 'Secret has been created!!!'
        Secret.objects.create(secret = postData['secret'], uploader = User.objects.get(id=user_id))
        return errors

    def process_like(self, postData):
        this_user = User.objects.get(id = postData['user_id'])
        this_secret = Secret.objects.get(id = postData['secret_id'])
        this_secret.liked_users.add(this_user)
        liked_users = Secret.objects.annotate(count_likes=Count('liked_users'))
        return liked_users

class Secret(models.Model):
    secret = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now= True)
    updated_at = models.DateTimeField(auto_now= True)
    uploader = models.ForeignKey(User, related_name='uploaded_secrets', on_delete=models.CASCADE)
    liked_users = models.ManyToManyField(User, related_name='liked_secrets')
    objects = SecretManager()
    def __repr__(self):
        return "<Secret: {}|{}>".format(self.id, self.secret)