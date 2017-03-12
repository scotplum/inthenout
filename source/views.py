from django.shortcuts import render,  get_object_or_404
import requests, datetime, feedparser

from .models import Source

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
	url = source_object.url
	oauth_version = source_object.oauth_version
	sourcename = {'name':source_object.name}
	urljson = {}
	if rss_flag:    
		if oauth_version == 0:
		    rssfeed(url)
	elif not rss_flag: 
		urljson = requests.get(url).json()
		context['api'] = urljson
	context['source'] = sourcename
	return render(request, 'source/details.html', {'JSON': context})
	
def apicall(url):
    urljson = requests.get(url).json()
    context['api'] = urljson	
    return context
	
def rssfeed(url):
    url_parsed = feedparser.parse(url)		
    url_parsed0 = url_parsed.entries[0]
    url_feed = url_parsed.feed
    context['entries'] = url_parsed0
    context['feed'] = url_feed
    return context 