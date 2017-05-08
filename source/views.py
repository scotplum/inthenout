from django.shortcuts import render,  get_object_or_404, redirect
import requests, datetime, feedparser
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Source, Source_Variable, Source_User, SourceUserForm, Source_Category
from collection.models import User_Collection
from django.contrib.auth.models import User

from inthenout.utils import apicall, navigationlinks

context = {}

def index(request):
	#Get all source objects
	sources = Source.objects.all()
	context = navigationlinks(request)
	#Assign context
	context['source_list'] = sources
	context['source_category'] = Source_Category.objects.all()
	context['source_organization'] = Source.objects.values('organization').distinct()
	return render(request, 'source/index.html', context)
	
def category(request, category):
	#Get all source objects
	sources = Source.objects.filter(category=category)
	context = navigationlinks(request)
	context['category'] = Source_Category.objects.filter(id=category)	
	context['source_list'] = sources
	return render(request, 'source/category.html',context)

def organization(request, organization):
	#Get all source objects
	sources = Source.objects.filter(organization=organization)
	context = navigationlinks(request)
	context['organization'] = organization 
	context['source_list'] = sources
	return render(request, 'source/organization.html',context)	
	
#The function below parses RSS feeds and API calls	
@login_required
def detail(request, source_id):
	#Assign variables
	user_object = request.user
	source_user_object = Source_User.objects.filter(user=user_object.id)
	collection_object = User_Collection.objects.filter(user=user_object.id)
	su_is_active = ""
	source_variable = []
	url_param = {}
	url_dict = {}
	user_object = request.user
	source_object = Source.objects.get(pk=source_id)
	source_var_check = Source_Variable.objects.filter(source_id=source_object.id).exists()
	source_user_check = Source_User.objects.filter(source=source_object.id).filter(user=user_object.id).exists()
	if source_user_check:
		#su_object = Source_User.objects.filter(source=source_object.id).filter(user=user_object.id)
		su_object = Source_User.objects.get(source=source_object.id, user=user_object.id)
		su_is_active = su_object.is_active
	if source_var_check:
		source_variable = Source_Variable.objects.filter(source_id=source_object.id).values('variable_name','variable_value')
	else:
		source_variable = []
	if request.method == "POST":
		form = SourceUserForm(request.POST)
		if not source_user_check:
			post = form.save(commit=False)
			post.user = user_object
			post.source = source_object
			post.date_created = timezone.now()
			post.is_active = True
			post.save()
			return redirect('/home/')
		else:
			su_object.is_active = not su_object.is_active
			su_object.save()
			return redirect('/home/')
	rss_flag = source_object.rss_flag
	dict0_flag = source_object.dict0_flag
	url = source_object.base_url
	oauth_version = source_object.oauth_version
	for dict in source_variable:
		url_param[str(dict['variable_name'])] = str(dict['variable_value'])
	sourcename = {'name':source_object.name}
	#Call function apicall to perform an api or rss call and parses the data into a flat format
	context = apicall(rss_flag, url, dict0_flag, sourcename, oauth_version, url_param)
	return render(request, 'source/details.html', {'JSON': context, 'su_check':source_user_check, 'su_is_active':su_is_active, 'object_list':source_user_object, 'collection_list':collection_object})