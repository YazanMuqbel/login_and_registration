from django.db import models
import re

# Create your models here.
from django.db import models

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First Name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last Name should be at least 2 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        if len(postData['password']) < 8:
            errors["password"] = "Password should be at least 8 characters"
        if postData['confirm_password'] != postData['password']:
            errors["password"] = "Passwords don't match"

            return errors


    

class User(models.Model):
    first_name = models.CharField(max_length=50) 
    last_name = models.CharField(max_length=50) 
    email = models.EmailField(max_length=150) 
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)

    objects = UserManager()