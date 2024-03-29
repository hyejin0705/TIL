from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # 참조할 때 이름
    followings = models.ManyToManyField('self', symmetrical = False, related_name='followers') 
