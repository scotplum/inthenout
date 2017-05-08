from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from source.models import Source_User, Source
from django.contrib.auth.decorators import login_required
from collection.models import User_Collection
from django.contrib.auth.models import User
from home.models import User_Variable
from inthenout.utils import navigationlinks
from forms import CustomUserDataForm

context = {}

# Create your views here.
@login_required
def home(request):
	context = navigationlinks(request)
	user_object = request.user
	context['custom_user_data'] = User_Variable.objects.filter(user_id=user_object.id)
	return render(request, 'home/index.html', context)
	
@login_required
def customdata(request):
	context = navigationlinks(request)
	user_object = request.user
	#Form Procesing
	if request.method == "POST":
	    form = CustomUserDataForm(request.POST)
	    if form.is_valid():
			post = form.save(commit=False)
			post.user_id = user_object.id
			post.date_created = timezone.now()
			post.is_active = True
			post.save()
			redirecturl = '/home/'
			return redirect(redirecturl)
	else:
		form_class = CustomUserDataForm
		context['form'] = form_class
		return render(request, 'home/customdata.html', context)	
	return render(request, 'home/customdata.html', context)