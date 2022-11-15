from django.db import models

statusinfo = (
        ('Online','Online'),
        ('Offline','Offline'),
    )
devicetype = (
        ('Raspberrypi3','Raspberrypi3'),
        ('Nvidia','Nvidia'),
        ('Raspberrypi4','Raspberrypi4')
    )

# Create your models here.
class User_Data(models.Model):
    username = models.CharField(max_length=50,blank=False)
    email = models.EmailField(max_length=50,blank=False)
    password1 = models.CharField(max_length=30,blank=False)
    password2 = models.CharField(max_length=30,blank=False)

class DeviceDetails(models.Model):
    userID = models.CharField(max_length=30)
    status = models.CharField(max_length=7,choices=statusinfo,default="Online")
    devicetype = models.CharField(max_length=30,choices=devicetype,default="UnKnown")
    name = models.CharField(max_length=30,blank=False,default="UnKnown")

