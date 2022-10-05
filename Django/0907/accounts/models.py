from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import AbstractBaseUser
# 처음부터 모델을 짜고 싶을 때에는 base폼으로 깔고 쓰는

# Create your models here.
class User(AbstractUser):
    pass
