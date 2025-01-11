from django.db import models
from django.contrib.auth.models import AbstractUser



class UserProfile(AbstractUser):

    image = models.ImageField(blank=True,upload_to='profile_image/')
    bio = models.TextField(blank=True, null=True)
