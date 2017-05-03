from django.shortcuts import render, get_object_or_404, redirect
import requests, datetime, feedparser
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from source.models import Source, Source_Variable, Source_User
from django.contrib.auth.models import User
from forms import CollectionForm
from inthenout.utils import apicall

context = {}

def index(request):
	#Get all source objects
	sources = Source.objects.all()
	#Get the object for this user and assign Source_User data
	user_object = request.user
	context['object_list'] = Source_User.objects.filter(user=user_object.id)
	return render(request, 'collection/index.html',context)

def add(request):
	#Get all source objects
	sources = Source.objects.all()
	#Get the object for this user and assign Source_User data
	user_object = request.user
	context['object_list'] = Source_User.objects.filter(user=user_object.id)
	#Form processing
	if request.method == "POST":
	    form = CollectionForm(request.POST)
	    if form.is_valid():
			post = form.save(commit=False)
			post.date_create = timezone.now()
			post.is_active = True
			post.is_public = False
			post.category = "General"
			post.created_by = user_object
			post.save()
			redirecturl = '/collection/' + str(post.id) + '/'
			return redirect(redirecturl)
	else:
		form_class = CollectionForm
		return render(request, 'collection/add.html', {
			'form': form_class,
		})	
	return render(request, 'collection/add.html', context)
	
def detail(request, collection_id):
	#Get all source objects
	sources = Source.objects.all()
	#Get the object for this user and assign Source_User data
	user_object = request.user
	context['object_list'] = Source_User.objects.filter(user=user_object.id)
	return render(request, 'collection/detail.html', context)