from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager


class User(AbstractUser):
    referral_token = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, blank=False, null=True)
    # redefining standard user manager
    objects = UserManager()
    #here to be aded
    # add new required field "referral_token"
    REQUIRED_FIELDS = ["referral_token", "email", "phone"]
    tasks = models.ManyToManyField("tasks.Task", through="tasks.TaskUserRel") 
