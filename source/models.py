import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.forms import ModelForm

class Source_Category(models.Model):
	name 			= models.CharField(max_length=50)
	date_created 	= models.DateTimeField(auto_now_add=True)
	description		= models.CharField(max_length=400)
	is_active		= models.BooleanField(default=True)
	
	def __str__(self):
		return self.name + " | " + self.description

class Source(models.Model):
	name 			= models.CharField(max_length=30)
	date_created 	= models.DateTimeField(auto_now_add=True)
	base_url 		= models.CharField(max_length=200)
	oauth_version	= models.IntegerField(default=0)
	rss_flag		= models.BooleanField(default=False)
	dict0_flag		= models.BooleanField(default=False)
	is_active		= models.BooleanField(default=True)
	description		= models.CharField(max_length=400)
	category		= models.ForeignKey(Source_Category, models.SET_NULL, blank=True, null=True,)
	organization	= models.CharField(max_length=100)
	
	def __str__(self):
		return self.name 

class Source_Variable(models.Model):
	source 			= models.ForeignKey(Source, on_delete=models.CASCADE)
	variable_name 	= models.CharField(max_length=100)
	variable_value 	= models.CharField(max_length=200)
	date_created 	= models.DateTimeField(auto_now_add=True)
	is_active 		= models.BooleanField(default=True)
	is_parameter 	= models.BooleanField(default=False)
	is_dummy 		= models.BooleanField(default=False)
	
	def __str__(self):
		return "{variable_name:" + self.variable_name + ",variable_value:" + self.variable_value + "}"
		#return str(self.source) + " " + self.variable_name + " " + self.variable_value}
		
class Source_User(models.Model):
	user 			= models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
	source 			= models.ForeignKey(Source, related_name='source', on_delete=models.CASCADE)
	date_created	= models.DateTimeField(auto_now_add=True)
	is_active		= models.BooleanField(default=True)
	
	def __str__(self):
		return str(self.source) + "_" + str(self.user)
		

class SourceUserForm(ModelForm):
    class Meta:
		model = Source_User
		exclude = ('user','source','date_created','is_active')
		
