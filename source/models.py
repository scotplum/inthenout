import datetime

from django.db import models
from django.utils import timezone

class Source(models.Model):
	name 			= models.CharField(max_length=30)
	date_created 	= models.DateTimeField('source creation date')
	url 			= models.CharField(max_length=200)
	key 			= models.CharField(max_length=200)
	secret 			= models.CharField(max_length=200)
	oauth_version	= models.IntegerField(default=0)
	url_call		= models.CharField(max_length=200)
	rss_flag		= models.BooleanField(default=False)
	dict0_flag		= models.BooleanField(default=False)
	is_active		= models.BooleanField(default=True)
	
	def __str__(self):
		return self.name + "  (Is Active:" + str(self.is_active) + ")"
