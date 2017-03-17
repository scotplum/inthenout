from django.shortcuts import render,  get_object_or_404
import requests, datetime, feedparser

from .models import Source
from flatten_json import flatten

context = {}

def index(request):
	sources = Source.objects.all()
	context = {'object_list':sources}
	return render(request, 'source/index.html', context)

#The function below parses RSS feeds and API calls	
def detail(request, source_id):
	context = {}
	source_object = Source.objects.get(pk=source_id)
	rss_flag = source_object.rss_flag
	dict0_flag = source_object.dict0_flag
	url = source_object.url
	oauth_version = source_object.oauth_version
	sourcename = {'name':source_object.name}
	urljson = {}
	if rss_flag:    
		url_parsed = feedparser.parse(url)		
		url_parsed0 = url_parsed.entries[0]
		url_feed = url_parsed.feed
		context['entries'] = flatten(url_parsed0)
		context['feed'] = flatten(url_feed)
	elif not rss_flag:
		url_api = {}
		if dict0_flag == 0:
			url_api['api'] = requests.get(url).json()
			context = flatten(url_api)	
		else:
			url_api['api'] = requests.get(url).json()[0]
			context = flatten(url_api)
		
	context['source'] = sourcename
	
	return render(request, 'source/details.html', {'JSON': context})
	

