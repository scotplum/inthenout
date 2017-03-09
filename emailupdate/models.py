import datetime

from django.db import models
from django.utils import timezone

class Email(models.Model):
	first_name = models.CharField(max_length=30)
	email_address = models.CharField(max_length=50)
	signup_date = models.DateTimeField('signup date')
	email_confirm = models.BooleanField

