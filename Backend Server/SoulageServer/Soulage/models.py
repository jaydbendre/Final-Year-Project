# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Data(models.Model):
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

    class Meta:
        managed = False
        db_table = 'data'
