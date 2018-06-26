from __future__ import unicode_literals
from django.db import models
import bcrypt
import re
from django.db.models import Count

EMAIL_REGEX = re.compile('^[_a-z0-9-]+(.[_a-z0-9-]+)@[a-z0-9-]+(.[a-z0-9-]+)(.[a-z]{2,4})$')
PASSWORD_REGEX = re.compile('^[A-Za-z0-9#!*@$%^&.()\-_]{8,32}$')


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
        if not re.match(PASSWORD_REGEX, postData['password']):
            errors['password'] = 'Password must be between 8 and 32 characters, and can contain numbers and the following split characters: #!*@$%^&()\-_.'
        if postData['password'] != postData['confirm']:
            errors['password'] = 'Passwords do not match.'
        if User.objects.filter(email = postData['email']):
            errors['email'] = 'Email already exists.'
        return errors

    def login_validator(self, postData):
        errors = {}
        if not User.objects.filter(email= postData['email']):
            errors['email'] = 'Account does not exist.'
            return errors
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

    def update_validator(self, postData):
        errors = {}
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
        if User.objects.filter(email = postData['email']):
            errors['email'] = 'Email already exists.'
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

QUOTE_REGEX = re.compile('^[A-Za-z0-9#!*@$%^&.()\ -_]{10,255}$')

class QuoteManager(models.Manager):
    def process_quote(self, postData, user_id):
        errors = {}
        user = User.objects.get(id=user_id)
        print("looking for errors in quote")
        if len(postData['author']) < 3:
            errors['author'] = "Author must be at least 3 characters"
        if not postData['author'].isalpha():
            errors['author'] = 'Author cannot contain non-alpha characters.'
        if not re.match(QUOTE_REGEX, postData['quote']):
            errors['quote'] = 'Quote must be between 10 and 255 charaters, and ca include the following: numbers, upper and lower case letters, and these split characters: #!*@$%^&()\-_.'
            return errors
        print(user.first_name, user.last_name,'is creating quote....')
        errors['quote'] = 'Quote has been created!!!'
        Quote.objects.create(text = postData['quote'], author= postData['author'], uploader = User.objects.get(id=user_id))
        return errors

    def process_like(self, postData, id):
        print("processing like")
        this_user = User.objects.get(id = id)
        this_quote = Quote.objects.get(id = postData['quote_id'])
        this_quote.liked_users.add(this_user)
        liked_users = Quote.objects.annotate(count_likes=Count('liked_users'))
        return liked_users

class Quote(models.Model):
    text = models.TextField(max_length=255)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now= True)
    updated_at = models.DateTimeField(auto_now= True)
    uploader = models.ForeignKey(User, related_name='uploaded_quote', on_delete=models.CASCADE)
    liked_users = models.ManyToManyField(User, related_name='liked_quotes')
    objects = QuoteManager()
    def __repr__(self):
        return "<Quote: {}|{}>".format(self.id, self.text)