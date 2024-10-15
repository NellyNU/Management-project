from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    STATUS_CHOICES = [
        ('ADMIN','Admin'),
        ('PROJECT_MANAGER','Project Manager'), 
        ('USER','User'),
    ]

    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    is_email_verified = models.BooleanField(default=False)
    role = models.CharField(max_length=20, choices=STATUS_CHOICES, default='USER')


    def __str__(self):
        return self.email


    

