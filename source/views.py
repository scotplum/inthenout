from django.shortcuts import render,  get_object_or_404
import requests, datetime, feedparser

from .models import Source

from inthenout.utils import apicall

context = {}

def index(request):
	sources = Source.objects.all()
	context = {'object_list':sources}
	return render(request, 'source/index.html', context)

#The function below parses RSS feeds and API calls	
def detail(request, source_id):
	#Assign variables
	source_object = Source.objects.get(pk=source_id)
	rss_flag = source_object.rss_flag
	dict0_flag = source_object.dict0_flag
	url = source_object.url
	oauth_version = source_object.oauth_version
	sourcename = {'name':source_object.name}
	#Call function apicall to perform an api or rss call and parses the data into a flat format
	context = apicall(rss_flag, url, dict0_flag, sourcename, oauth_version)
	return render(request, 'source/details.html', {'JSON': context})