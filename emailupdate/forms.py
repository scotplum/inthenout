from django import forms
from django.forms import ModelForm
from models import Email

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Fieldset
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from crispy_forms.bootstrap import TabHolder, Tab

# Email Update Form
class EmailForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(EmailForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'id-email-signup-form'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'
        self.helper.add_input(Submit('submit', 'Sign Up'))
		
	def __str__(self):
		return 'Email: %s | First Name: %s' % (self.email_address, self.first_name)
	
    class Meta:
		model = Email
		fields = ('first_name', 'email_address',)