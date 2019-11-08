from django.db import models

# Create your models here.

class UserProfile(models.Model):

    user_id = models.CharField(max_length=50, unique=True)
    user_city = models.CharField(max_length=25)
    user_number = models.CharField(max_length=10)
    user_picture = models.CharField(max_length=250, blank=True,null=True, default=None)

