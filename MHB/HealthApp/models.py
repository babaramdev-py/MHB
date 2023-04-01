from django.db import models
from django.contrib.auth.models import User
import openai
openai.api_key = "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"

messages = [{"role": "system", "content": "You are an empathetic friend that listens and provides guidance only, you respond to no other questions other than emotional ones."}]

# Create your models here.

class User(models.Model):
    user = models.OneToOneField(User, 
    on_delete=models.CASCADE,
    primary_key=True)
    username = models.CharField(max_length=256,unique=True,blank=False,null=True)
    concerns = models.CharField(max_length=256)
    def __str__(self):
        return "{}".format(self.user)



class Therapist(models.Model):
    full_name = models.CharField(null = False,blank = False,max_length=80)
    phone = models.IntegerField(null = False,blank = False,unique = True)
    email = models.EmailField(unique=True, max_length=254)
    yoe = models.IntegerField(blank=False)