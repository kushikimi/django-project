from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class user_profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio=models.URLField(blank=True,null=True)
    profile_pic=models.ImageField(blank=True,upload_to='media',null=True)

    def __str__(self):
        return self.user.username
