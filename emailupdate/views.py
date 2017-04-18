from django.shortcuts import render, get_object_or_404, redirect
#from emailupdate.forms import emailupdate_form
from .models import EmailForm
from django.utils import timezone

def index(request):
	if request.method == "POST":
		form = EmailForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.signup_date = timezone.now()
			post.email_confirmed = True
			post.save()
			return redirect('/emailupdate/thanks/')
	else:
		form_class = EmailForm
		return render(request, 'emailupdate/emailupdate.html', {
			'form': form_class,
		})	
		
def thanks(request):
	return render(request, 'emailupdate/emailupdate_thanks.html')