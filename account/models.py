from pyexpat import model
from time import time
from xml.dom.domreg import registered
from django.db import models

from django.utils import timezone

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=10)
    age = models.IntegerField(null=True)
    state = models.CharField(max_length=255)
    regd_as = models.CharField(max_length=255)
    professional_opted_for = models.CharField(max_length=255, null=True, blank= True)
    date_joined = models.DateTimeField(default=timezone.now)

    # subscribtion_status = models.BooleanField(default=False)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return self.email


class UserOtp(models.Model):

    user = models.ForeignKey(CustomUser, on_delete= models.CASCADE)
    time_stamp = models.DateTimeField(auto_now= True)
    otp = models.IntegerField()

class ForgetPassword(models.Model):

    user = models.ForeignKey(CustomUser, on_delete= models.CASCADE)
    forget_password_token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.user.email

