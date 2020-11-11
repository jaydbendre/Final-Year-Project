from django.db import models
import datetime

# Create your models here.


class user(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    twitter_user_name = models.CharField(max_length=50, unique=True)
    email = models.EmailField
    password = models.CharField(max_length=50)
    location = models.Choices(max_length=50)
    date_of_birth = models.DateField(default=None)
    otp = models.CharField(max_length=10)
    otp_time_stamp = models.DateTimeField(default=datetime.datetime.now())
    is_verified = models.BooleanField(default=False)
    role = models.IntegerField(default=1)


class
