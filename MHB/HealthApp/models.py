from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User(models.Model):
    user = models.OneToOneField(User, 
    on_delete=models.CASCADE,
    primary_key=True)
    concerns = models.CharField(max_length=256)


class Therapists(models.Model):
    full_name = models.CharField(null = False,blank = False,max_length=80)
    phone = models.IntegerField(null = False,blank = False,unique = True)
    email = models.EmailField(unique=True, max_length=254)
    yoe = models.IntegerField(blank=False)