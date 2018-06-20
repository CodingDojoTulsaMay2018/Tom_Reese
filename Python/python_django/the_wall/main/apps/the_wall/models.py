from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        print("*********validator is checking for errors")
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
            if len(postData['password']) > 200:
                errors['password'] = "Password can only be up to two-hundred characters"
            if postData['password'] != postData['password_confirm']:
                errors['password'] = "Password must match Password Confirmation"
            if not EMAIL_REGEX.match(postData['email']):
                errors['email'] = "Email must fit valid format"
            if User.objects.filter(email = postData['email']):
                errors['email'] = 'Email already exists.'
            return errors
        else:
            print("returning user")
            user = User.objects.filter(email=postData['email'])
            print(user)
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
                print("user not found")
                errors['email'] = "Account not found"
                return errors



class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=200, default="password1")
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<User: {} |{} {} {} {} {}>".format(self.id, self.first_name, self.last_name, self.email, self.password, self.created_at)
    objects = UserManager()

class Review(models.Model):
    message = models.TextField(max_length=1000)
    user = models.ForeignKey(User, related_name="has_reviews", blank=True)
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<Review: {} | {} {}>".format(self.id, self.message, self.created_at)
    # objects = UserManager()

class Comment(models.Model):
    message = models.TextField(max_length=1000)
    user = models.ForeignKey(User, related_name="has_comments", blank=True)
    review = models.ForeignKey(Review, related_name="has_comments", blank=True)
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<Comment: {} | {} {}>".format(self.id, self.message, self.created_at)
    # objects = UserManager()