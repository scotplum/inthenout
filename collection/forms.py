from django import forms
from django.forms import ModelForm
from models import Collection, Collection_Variable

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Fieldset
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from crispy_forms.bootstrap import TabHolder, Tab

# Collection Addition Form
class CollectionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CollectionForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Collection Name"
        self.helper = FormHelper(self)
        self.helper.form_id = 'id-collection-add-form'
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal w3-forms'
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.layout = Layout(
            Div(
				'name',
				'description',
				'category'
				)
			)
			
	def __str__(self):
		return 'Name: %s | Description: %s' % (self.name, self.description)
	
    class Meta:
		model = Collection
		fields = ('name', 'description', 'category',)

# Adding Collection Variables
class CustomCollectionDataForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CustomCollectionDataForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'id-collection-variable-form'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'
        self.helper.add_input(Submit('submit', 'Save'))
		
	def __str__(self):
		return 'Variable Name: %s | Variable Value: %s | Is Active: %s' % (self.variable_name, self.variable_value, self.is_active)
	
    class Meta:
		model = Collection_Variable
		fields = ('variable_name', 'variable_value',)
		