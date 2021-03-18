# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import datetime

# Create your models here.


class Data_Collection(models.Model):
    id = models.BigIntegerField(primary_key=True)
    text = models.TextField(blank=True, null=True)
    created_at = models.TextField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    user_name = models.TextField(blank=True, null=True)
    verfied = models.IntegerField(blank=True, null=True)
    geo = models.TextField(blank=True, null=True)
    quoted = models.BigIntegerField(blank=True, null=True)
    favorite = models.BigIntegerField(blank=True, null=True)
    retweet = models.BigIntegerField(blank=True, null=True)
    place = models.TextField(blank=True, null=True)
    coordinates = models.TextField(blank=True, null=True)
    media_type = models.TextField(blank=True, null=True)
    media_url = models.TextField(blank=True, null=True)
    media_id = models.FloatField(blank=True, null=True)
    rt = models.IntegerField(blank=True, null=True)
    rt_username = models.TextField(blank=True, null=True)
    stored_at = models.DateTimeField(default=datetime.datetime.now())


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    twitter_user_name = models.CharField(max_length=50, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    date_of_birth = models.DateField(default=None)
    otp = models.CharField(max_length=10)
    otp_time_stamp = models.DateTimeField(default=datetime.datetime.now())
    is_verified = models.BooleanField(default=False)
    verified_at = models.DateTimeField(default=datetime.datetime.now())
    role = models.IntegerField(default=1)


class Organisations(models.Model):
    org_name = models.CharField(max_length=50)
    typeOrg = models.IntegerField()
    is_verified = models.BooleanField(default=False)
    location = models.CharField(max_length=50)
    joining_time = models.DateTimeField()
    POC_user = models.ForeignKey(User, on_delete=models.CASCADE)


class User_Organisation_Map(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    org_id = models.ForeignKey(Organisations, on_delete=models.CASCADE)


class Topics(models.Model):
    topic_name = models.CharField(max_length=50)
    keywords = models.CharField(max_length=200, default=None)
    # alias = models.CharField(max_length=50, default=None)
    ignore_flag = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.datetime.now())


class Topic_Tweet_Map(models.Model):
    tweet_id = models.ForeignKey(Data_Collection, on_delete=models.CASCADE)
    topic_id = models.ForeignKey(Topics, on_delete=models.CASCADE)


class Tweet_Sentiment(models.Model):
    tweet_id = models.ForeignKey(Data_Collection, on_delete=models.CASCADE)
    empty = models.DecimalField(default=None, max_digits=5, decimal_places=2)
    sadness = models.DecimalField(default=None, max_digits=5, decimal_places=2)
    enthusiasm = models.DecimalField(
        default=None, max_digits=5, decimal_places=2)
    neutral = models.DecimalField(default=None, max_digits=5, decimal_places=2)
    worry = models.DecimalField(default=None, max_digits=5, decimal_places=2)
    surprise = models.DecimalField(
        default=None, max_digits=5, decimal_places=2)
    love = models.DecimalField(default=None, max_digits=5, decimal_places=2)
    fun = models.DecimalField(default=None, max_digits=5, decimal_places=2)
    hate = models.DecimalField(default=None, max_digits=5, decimal_places=2)
    happiness = models.DecimalField(
        default=None, max_digits=5, decimal_places=2)
    boredom = models.DecimalField(default=None, max_digits=5, decimal_places=2)
    relief = models.DecimalField(default=None, max_digits=5, decimal_places=2)
    anger = models.DecimalField(default=None, max_digits=5, decimal_places=2)


class Tweet_Image_class(models.Model):
    tweet_id = models.ForeignKey(Data_Collection, on_delete=models.CASCADE)
    Explicit = models.DecimalField(
        default=None, max_digits=5, decimal_places=2)
    Meme = models.DecimalField(default=None, max_digits=5, decimal_places=2)
    Nature = models.DecimalField(default=None, max_digits=5, decimal_places=2)
    Other = models.DecimalField(default=None, max_digits=5, decimal_places=2)
    Poster = models.DecimalField(default=None, max_digits=5, decimal_places=2)
    Potrait = models.DecimalField(default=None, max_digits=5, decimal_places=2)
    Protests = models.DecimalField(
        default=None, max_digits=5, decimal_places=2)
    cyclone = models.DecimalField(default=None, max_digits=5, decimal_places=2)
    earthquake = models.DecimalField(
        default=None, max_digits=5, decimal_places=2)
    flood = models.DecimalField(default=None, max_digits=5, decimal_places=2)
    wildfire = models.DecimalField(
        default=None, max_digits=5, decimal_places=2)


class Request(models.Model):
    topic_id = models.ForeignKey(Topics, on_delete=models.CASCADE)
    org_id = models.ForeignKey(Organisations, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    is_approved = models.BooleanField(default=0)
    is_active = models.BooleanField(default=0)
    initiated_at = models.DateTimeField(default=datetime.datetime.now())
    decision_passed_at = models.DateTimeField(default=datetime.datetime.now())


class Donations (models.Model):
    request_id = models.ForeignKey(Request, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    donate = models.TextField(default=None)
    donated_at = models.DateTimeField(default=datetime.datetime.now())
    is_complete = models.BooleanField(default=False)


class POC_requests(models.Model):
    name = models.TextField(default=None)
    organisation_details = models.TextField(default=None)
    is_approved = models.BooleanField(default=False)
    decision_passed_at = models.DateTimeField(default=datetime.datetime.now())
    email = models.EmailField(unique=True)
