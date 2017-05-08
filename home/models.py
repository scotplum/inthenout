from __future__ import unicode_literals
from django.utils import timezone
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.db import models

# Create your models here.

class User_Variable(models.Model):
	user	 		= models.ForeignKey(User, on_delete=models.CASCADE)
	variable_name 	= models.CharField(max_length=100)
	variable_value 	= models.CharField(max_length=500)
	date_created 	= models.DateTimeField(auto_now_add=True)
	is_active 		= models.BooleanField(default=True)
	
	def __str__(self):
		return "variable_name: " + self.variable_name + " | variable_value: " + self.variable_value + " | collection: " + str(self.user.id)