
from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

class Message(models.Model):
    message = models.JSONField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)
    class Meta:
        ordering = ['message']



class USER(models.Model):
    addhar_no=models.CharField(max_length=10000, default="")

    name=models.CharField(max_length=10000, default="")
    curr_location=models.CharField(max_length=10000, default="")
    blood_group=models.CharField(max_length=10000, default="")
    age=models.CharField(max_length=10000, default="")
    gender=models.CharField(max_length=10000, default="")
    



# Create your models here.
class HOSPITALS(models.Model):
    name=models.CharField(max_length=10000, default="")
    beds=models.IntegerField(default=0)
    icu=models.IntegerField(default=0)
    location=models.CharField(max_length=100,default="")
    no_of_doc=models.IntegerField(default=0)
    no_of_nurse=models.IntegerField(default=0)
    a_pve=models.IntegerField(default=0)
    a_nve=models.IntegerField(default=0)
    ab_nve=models.IntegerField(default=0)
    ab_pve=models.IntegerField(default=0)
    b_pve=models.IntegerField(default=0)
    b_nve=models.IntegerField(default=0)
    o_nve=models.IntegerField(default=0)
    o_pve=models.IntegerField(default=0)
    class Meta:
        ordering = ['name']
class BLOODBANK(models.Model):
    name=models.CharField(max_length=10000, default="")
    location=models.CharField(max_length=100,default="")
    a_pve=models.IntegerField(default=0)
    a_nve=models.IntegerField(default=0)
    ab_nve=models.IntegerField(default=0)
    ab_pve=models.IntegerField(default=0)
    b_pve=models.IntegerField(default=0)
    b_nve=models.IntegerField(default=0)
    o_nve=models.IntegerField(default=0)
    o_pve=models.IntegerField(default=0)

    class Meta:
        ordering = ['name']

class MEDICINE(models.Model):
    name=models.CharField(max_length=1000, default="")
    hospital=models.IntegerField(default=0)
    quantity=models.IntegerField(default=0)
    

class DISTANCE(models.Model):
    hid=models.IntegerField()
    dist=models.IntegerField()

        

       