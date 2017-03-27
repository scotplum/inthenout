from django.shortcuts import render,  get_object_or_404
import requests, datetime, feedparser

from .models import Source, Source_Variable

from inthenout.utils import apicall

context = {}

def index(request):
	sources = Source.objects.all()
	context = {'object_list':sources}
	return render(request, 'source/index.html', context)

#The function below parses RSS feeds and API calls	
def detail(request, source_id):
	#Assign variables
	source_variable = []
	url_param = {}
	url_dict = {}
	source_object = Source.objects.get(pk=source_id)
	source_var_check = Source_Variable.objects.filter(source_id=source_object.id).exists()
	if source_var_check:
		source_variable = Source_Variable.objects.filter(source_id=source_object.id).values('variable_name','variable_value')
	else:
		source_variable = []
	rss_flag = source_object.rss_flag
	dict0_flag = source_object.dict0_flag
	url = source_object.base_url
	oauth_version = source_object.oauth_version
	for dict in source_variable:
		url_param[str(dict['variable_name'])] = str(dict['variable_value'])
	sourcename = {'name':source_object.name}
	#Call function apicall to perform an api or rss call and parses the data into a flat format
	context = apicall(rss_flag, url, dict0_flag, sourcename, oauth_version, url_param)
	return render(request, 'source/details.html', {'JSON': context})