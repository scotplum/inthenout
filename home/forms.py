from django import forms
from django.forms import ModelForm
from models import User_Variable

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Fieldset
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from crispy_forms.bootstrap import TabHolder, Tab

# Adding Collection Variables
class CustomUserDataForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserDataForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'id-user-variable-form'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'
        self.helper.add_input(Submit('submit', 'Save'))
		
	def __str__(self):
		return 'Variable Name: %s | Variable Value: %s | Is Active: %s' % (self.variable_name, self.variable_value, self.is_active)
	
    class Meta:
		model = User_Variable
		fields = ('variable_name', 'variable_value',)