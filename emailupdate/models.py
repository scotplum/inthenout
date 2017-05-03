import datetime

from django.db import models
from django.utils import timezone
from django.forms import ModelForm

class Email(models.Model):
	first_name = models.CharField(max_length=30)
	email_address = models.EmailField(max_length=50, unique=True)
	signup_date = models.DateTimeField('signup date')
	email_confirm = models.BooleanField
	
	def __str__(self):
		return 'Email: %s | First Name: %s' % (self.email_address, self.first_name)

'''
class EmailForm(ModelForm):
    class Meta:
		model = Email
		fields = ('first_name', 'email_address',)
'''