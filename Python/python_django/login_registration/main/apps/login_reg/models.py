from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        print(postData['log_type'],"************************is the login typ")
        if postData['log_type'] == "registered!":
            if not postData['first_name'].isalpha():
                errors['first_name'] = 'First name contains non-alpha characters.'
            if len(postData['first_name']) < 2:
                errors['first_name'] = 'First name should be at least 2 characters.'
            if len(postData['last_name']) < 2:
                errors['last_name'] = 'Last name should be at least 2 characters.'
            if not postData['last_name'].isalpha():
                errors['last_name'] = 'Last name contains non-alpha characters.'
            if len(postData['password']) < 8:
                errors['password'] = "Password needs to be at least eight characters"
            if len(postData['password']) > 20:
                errors['password'] = "Password can only be up to twenty characters"
            if postData['password'] != postData['password_confirm']:
                errors['password'] = "Password must match Password Confirmation"
            if not EMAIL_REGEX.match(postData['email']):
                errors['email'] = "Email must fit valid format"
            if User.objects.filter(email = postData['email']):
                errors['email'] = 'Email already exists.'
            return errors
        else:
            user = User.objects.filter(email=postData['email'])
            if user:
                user = User.objects.get(id=user[0].id)
                print(user,"is the user")
                if bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                    print("password match")
                    return errors
                else:
                    print("failed password")
                    errors['password'] = "Password is incorrect"
                return errors
            else:
                errors['email'] = "Invalid Email"
                return errors
        return errors



            
        

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<User: {} |{} {} {} {} {}>".format(self.id, self.first_name, self.last_name, self.email, self.password, self.created_at)
    objects = UserManager()
