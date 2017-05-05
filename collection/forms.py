from django import forms
from django.forms import ModelForm
from models import Collection

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Fieldset
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from crispy_forms.bootstrap import TabHolder, Tab

# Email Update Form
class CollectionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CollectionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'id-email-signup-form'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'
        self.helper.add_input(Submit('submit', 'Sign Up'))
		
	def __str__(self):
		return 'Name: %s | Description: %s' % (self.name, self.description)
	
    class Meta:
		model = Collection
		fields = ('name', 'description', 'category',)