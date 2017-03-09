import datetime

from django.db import models
from django.utils import timezone

class Source(models.Model):
	source_name = models.CharField(max_length=30)
	source_creation_date = models.DateTimeField('source creation date')
	source_url = models.CharField(max_length=200)
	def __str__(self):
		return self.source_name
		return self.source_url