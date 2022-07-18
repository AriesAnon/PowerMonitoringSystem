from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AppliancesManagement(models.Model):
    applianceid = models.AutoField(db_column='applianceID', primary_key=True)  # Field name made lowercase.
    appliancename = models.CharField(db_column='applianceName', max_length=255)  # Field name made lowercase.
    appliancerating = models.IntegerField(db_column='applianceRating', blank=True, null=True)  # Field name made lowercase.
    roomid = models.ForeignKey('RoomManagement', models.DO_NOTHING, db_column='roomID', blank=True, null=True)  # Field name made lowercase.   

    class Meta:
        managed = False
        db_table = 'appliances_management'


class RoomManagement(models.Model):
    roomid = models.AutoField(db_column='roomID', primary_key=True)  # Field name made lowercase.
    roomnum = models.IntegerField(db_column='roomNum')  # Field name made lowercase.
    roomname = models.CharField(db_column='roomName', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'room_management'