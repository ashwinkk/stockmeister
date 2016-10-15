from django.db import models

# Create your models here.

class User(models.Model):
	uname = models.CharField(max_length=50,primary_key=True)
	password = models.CharField(max_length=50)
	portfolios = models.CharField(max_length=1000,null=True,blank=True)
	name = models.CharField(max_length=50)
	emailid = models.EmailField(max_length=40)