from django import forms

# Email Update Form
class emailupdate_form(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(emailupdate_form, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "First name:"
        self.fields['contact_email'].label = "Email address:"
