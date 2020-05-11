
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.
#Signedup users model
class User(AbstractUser):
    # autogenerated userId
    #userId = models.CharField(max_length=255, null=False)
    # username
    username = models.CharField(max_length=255, unique=True)
     # Email userId
    email = models.CharField(max_length=255, null=False)
    # Address
    #address = models.CharField(max_length=1024, null=False)
    # Role 
    #role = models.CharField(max_length=255, null=False)
    # password
    password = models.CharField(max_length=1024, null=False)
    # status of registration approval
   # status = models.CharField(max_length=1024, null=False)
    password2 = models.CharField(max_length=1024, null=False)
    USERNAME_FIELD = 'username'
    def __str__(self):
        return "{} - {}".format(self.username, self.email)

#Sites Added by Admin model
class Site(models.Model):
    # autogenerated SiteId unique
    siteId = models.CharField(max_length=255, null=False, primary_key=True)
    # sitename
    siteName = models.CharField(max_length=255, null=False, unique=True)
     # sitelocation
    siteLocation = models.CharField(max_length=1024, null=False)
    # Site Info
    siteInfo = models.CharField(max_length=1024, null=False)
   
    def __str__(self):
        return "{} - {}".format(self.siteId, self.siteName, self.siteLocation, self.siteInfo)

#Site activity

class SiteActivity(models.Model):
    # autogenerated SiteId unique
    siteActivityId = models.CharField(max_length=255, null=False)
    # site activity name
    activityName = models.CharField(max_length=255, null=False)
     # site id foreign key for sites table's siteid
    siteId = models.ForeignKey('Site', on_delete=models.CASCADE)
    # Site Activity Info
    activityInfo = models.CharField(max_length=1024, null=False)
   
    def __str__(self):
        return "{} - {}".format(self.siteActivityid, self.activityName, self.siteId, self.ActivityInfo)
   
#activity report type model
class SiteActivityType(models.Model):
    # Site activity type id.
    siteActivityTypeId = models.CharField(max_length=255, null=False)
    # Fields to be reported. Json stored as string. should be converted back to json when fetched.
    reportingFields = models.CharField(max_length=1024, null=False)
    # site activity id is foreign key of SiteActivities model.
    siteActivityId = models.ForeignKey('SiteActivity', on_delete=models.CASCADE)
    # Site Activity Info.
    activityTypeInfo = models.CharField(max_length=1024, null=False)
   
    def __str__(self):
        return "{} - {}".format(self.siteActivityTypeId, self.reportingFields, self.siteActivityId, self.activityTypeInfo)
    
# Model for saving reports. All reports will be stored in one model irrespective of the type of the site activity selected
#reducing the burden of creating a model specific to the new activity type when added in future. when a new site activity is added with three fields the three
# can be added to the below model. As per business there wont be any new field added
# while saving to a report fetch the activity type json and save only them but not any in the api even if more fields are recieved.
#userID, siteId, siteActivityId, dia, fromNode, toNode, numberOfManholesErected,
#manholeId, remarks, distance, width, UPVCDia, MHDia, UPVCLength, ICChambersInstalled,
#reason, status
class Report(models.Model):
    # ReportId is auto generated upon creation.
    reportId = models.CharField(max_length=255, null=False)
    # userId of the user who created the report.
    username = models.CharField(max_length=1024, null=False)
    # site for which the report is generated.
    siteId = models.CharField(max_length=1024, null=False)
    # Activity for which the report is generated.
    siteActivityId = models.CharField(max_length=1024, null=False)
    #Dia dropdown{150MM, 200MM etc)
    dia = models.CharField(max_length=255, null=False)
    #From Node
    fromNode =  models.CharField(max_length=255, null=False)
    #To Node
    toNode = models.CharField(max_length=255, null=False)
    #number of manholes erected
    numberOfManholesErected = models.CharField(max_length=255, null=False)
    #Manhole Id
    manholeId = models.CharField(max_length=255, null=False)
    #Remarks 
    remarks = models.CharField(max_length=1024, null=False)
    #Distance
    distance = models.CharField(max_length=255, null=False)
    #Width
    width = models.CharField(max_length=1024, null=False)    
        #UPVC DIA Dropdown
    UPVCDia = models.CharField(max_length=1024, null=False)
    #Manhole DIA Dropdown
    MHDia = models.CharField(max_length=1024, null=False)
        #Remember to ask user to select node or manholeId
    #Node/MHID = models.CharField(max_length=1024, null=False)
        #lengthofUPVC pipe Laid
    UPVCLength = models.CharField(max_length=1024, null=False)    
        #Ic Chanbers Installed Dropdown
    ICChambersInstalled = models.CharField(max_length=1024, null=False)
        #hindrance reason
    reason = models.CharField(max_length=1024, null=False)
    # status of the report approved aor awaiting or rejected.
    status = models.CharField(max_length=1024, null=False)
    def __str__(self):
        return "{} - {}".format(self.reportId, self.userID, self.siteId, self.siteActivityId, self.dia, self.fromNode, self.toNode, self.numberOfManholesErected, self.manholeId,
                                self.remarks, self.distance, self.width, self.UPVCDia, self.UPVCLength, self.ICChambersInstalled, self.reason, self.MHdia)
    

#Dia Dropdown static table
    

class PipeLineDIA(models.Model):
    # ReportId is auto generated upon creation.
    PLDia = models.CharField(max_length=255, null=False)
    def __str__(self):
        return "{} - {}".format(self.PLDia)
#Dia Dropdown static table

class MHDIA(models.Model):
    # ReportId is auto generated upon creation.
    MHDia = models.CharField(max_length=255, null=False)
    def __str__(self):
        return "{} - {}".format(self.MHDia)
#Dia Dropdown static table

class UPVCDIA(models.Model):
    # ReportId is auto generated upon creation.
    UPVCDia = models.CharField(max_length=255, null=False)
    def __str__(self):
        return "{} - {}".format(self.UPVCDia)
#Dia Dropdown static table

class ICChamber(models.Model):
    # ReportId is auto generated upon creation.
    ICChamber = models.CharField(max_length=255, null=False)
    def __str__(self):
        return "{} - {}".format(self.ICChambers)
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

    

    
