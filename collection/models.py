from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.

class Collection_Category(models.Model):
	name 			= models.CharField(max_length=50)
	date_created 	= models.DateTimeField(auto_now_add=True)
	description		= models.CharField(max_length=400)
	is_active		= models.BooleanField(default=True)
	
	def __str__(self):
		return self.name

class Collection(models.Model):
	name 			= models.CharField(max_length=50)
	date_created 	= models.DateTimeField(auto_now_add=True)
	is_active		= models.BooleanField(default=True)
	description		= models.CharField(max_length=400)
	category		= models.ForeignKey(Collection_Category, models.SET_NULL, blank=True, null=True,)
	created_by		= models.ForeignKey(User, related_name='collection_user', on_delete=models.CASCADE)
	is_public		= models.BooleanField(default=False)
	
	def __str__(self):
		return self.name 
		
class Collection_Variable(models.Model):
	collection 		= models.ForeignKey(Collection, on_delete=models.CASCADE)
	variable_name 	= models.CharField(max_length=100)
	variable_value 	= models.CharField(max_length=500)
	date_created 	= models.DateTimeField(auto_now_add=True)
	is_active 		= models.BooleanField(default=True)
	
	def __str__(self):
		return "{variable_name:" + self.variable_name + ",variable_value:" + self.variable_value + "}"