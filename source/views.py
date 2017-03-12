from django.shortcuts import render,  get_object_or_404
import requests, datetime, feedparser

from .models import Source

def index(request):
	sources = Source.objects.all()
	context = {'object_list':sources}
	return render(request, 'source/index.html', context)
	
#Call Quotes API
def quotes(request):
    url = 'http://quotes.rest/qod.json'
    urljson = requests.get(url).json()
    urldict = urljson['contents']
    quotes = urldict['quotes']
    quotes0 = quotes[0]
    quotes_keys = quotes0.keys()
    return render(request, 'source/quotes.html', {'JSON': urldict})

#Parse RSS Feed
def rssfeed(request):
    url = 'http://feeds.feedburner.com/TheWirecutter'
    url_parsed = feedparser.parse(url)
    url_parsed0 = url_parsed.entries[0]
    feed_title = url_parsed.feed.title
    feed_description =  url_parsed.feed.description
    item_0_title = url_parsed.entries[0].title
    item_0_link = url_parsed.entries[0].link 
    context = {}
    context["feed_title"] = feed_title
    context["feed_description"] = feed_description
    context["item_title"] = item_0_title
    context["item_link"] = item_0_link
    return render(request, 'source/rssfeed.html', {'JSON': context})

#Parse Source Content (THIS IS NOT IN USE..See Detail for current use)

def sourcecontent(request):
    url = 'http://feeds.feedburner.com/TheWirecutter'
    url_parsed = feedparser.parse(url)
    url_parsed0 = url_parsed.entries[0]
    url_feed = url_parsed.feed
    context = {}
    context['entries'] = url_parsed0
    context['feed'] = url_feed
    return render(request, 'source/sourcecontent.html', {'JSON': context})

#The function below parses RSS feeds and API calls	
def detail(request, source_id):
	source_object = Source.objects.get(pk=source_id)
	rss_flag = source_object.rss_flag
	url = source_object.url
	oauth_version = source_object.oauth_version
	sourcename = {'name':source_object.name}
	context = {}
	urljson = {}
	if rss_flag:    
	    url_parsed = feedparser.parse(url)		
	    url_parsed0 = url_parsed.entries[0]
	    url_feed = url_parsed.feed
	    context['entries'] = url_parsed0
	    context['feed'] = url_feed
	#Get api info (need to add code to parse calls with more than one set of data calls that only have 1 set)
	elif not rss_flag: 
		urljson = requests.get(url).json()
		context['api'] = urljson
	context['source'] = sourcename
	return render(request, 'source/details.html', {'JSON': context})