from django.db import models
from django.contrib.auth.models import User    ####   Importing User model
# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User)  # Creating one to one relationship with model User so that we can add more Field
    # User is inbuilt model in Django
    #additional Field inserting here
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to = 'profile_pics',blank=True)

    def __str__(self):    #  printing the default string
        return self.user.username     #  username is the default of User model

# class UserFormName(models.Model):
#     user = models.OneToOneField(User)
#     uname = models.CharField(blank=True)
#     dir_name = models.CharField(blank=True)
#     size = models.IntegerField(blank=True)
