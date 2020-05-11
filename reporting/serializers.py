from rest_framework import serializers
from .models import (User, Site, SiteActivity,
SiteActivityType, Report, PipeLineDIA, MHDIA, UPVCDIA, ICChamber)

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Q

class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={}, write_only = True)
    class Meta:
        model = User
        fields = ( "username", "email",  "password",
                  "password2")
        extra_kwargs = {'password': {'write_only': True}}
    def save(self):
        user = User(email = self.validated_data['email'],
                     username=self.validated_data['username'],
                     )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        if password !=password2:
            raise serializers.ValidationError({'password': 'passwords must match'})
        user.set_password(password)
        user.save()
        return user


   
class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = ("siteId ","  siteName ","  siteLocation ","  siteInfo")   
    def save(self):
        site = Site(siteName = self.validated_data['siteName'],
                     siteLocation=self.validated_data['siteLocation'],
                    siteInfo=self.validated_data['siteInfo'],
                     )
        site.save()
        return site

class SiteActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteActivity
        fields = ("siteActivityId","activityName ","  siteId ","  ActivityInfo")
    

class SiteActivityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteActivityType
        fields = ("siteActivityTypeId ","  reportingFields ","  siteActivityId ","  activityTypeInfo")
   
class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ("reportId ","  userID ","  siteId ","  siteActivityId ","  dia ","  fromNode ","  toNode ","  numberOfManholesErected ","  manholeId ","  remarks ","  distance ","  width ","  UPVCDia ","  UPVCLength ","  ICChambersInstalled ","  reason ","  MHdia")

    

class PipeLineDIASerializer(serializers.ModelSerializer):
    class Meta:
        model = PipeLineDIA
        fields = ("PLDia")
        
class MHDIASerializer(serializers.ModelSerializer):
    class Meta:
        model = MHDIA
        fields = ("MHDia")

class UPVCDIASerializer(serializers.ModelSerializer):
    class Meta:
        model = UPVCDIA
        fields = ("UPVCDia")
   

class ICChamberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ICChamber
        fields = ("ICChambers")
