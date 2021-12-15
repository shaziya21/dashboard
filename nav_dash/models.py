from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    bot_name = models.CharField(max_length=200,primary_key=True)
    primary_color= models.CharField(max_length=200, null=True,blank=True)
    secondary_color= models.CharField(max_length=200, null=True,blank=True)
    accent_color= models.CharField(max_length=200, null=True,blank=True)
    profile_pic = models.ImageField(default="image.jpg", null=True, blank=True)

    def __str__(self):
        return self.primary_color
    

class Signup(models.Model):
    user = models.OneToOneField(User, null=True,on_delete=models.CASCADE)
    email = models.CharField(max_length=200,null=True)

class homescreen(models.Model):
    greetings=models.CharField(max_length=200, null=True,blank=True)
    conv= models.CharField(max_length=200, null=True,blank=True)
    button=models.BooleanField(default=False)

class suggestions(models.Model):
    Always = '0'

    Never = '1'

    Attempt= '2'

    SUPPORT_CONNECTION = [

        ( Always, 'Always'),

        (Never, 'Never'),

        (Attempt, 'After one failed attempt'),

    ]

    radio_support = models.CharField(max_length=3, choices=SUPPORT_CONNECTION, default=Always)
    button=models.BooleanField(default=False)
   

     






