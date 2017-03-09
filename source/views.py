from django.shortcuts import render
import requests, datetime, feedparser

def index(request):
    context = {}
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

#Parse Source Content
def sourcecontent(request):
    url = 'http://feeds.feedburner.com/TheWirecutter'
    url_parsed = feedparser.parse(url)
    url_parsed0 = url_parsed.entries[0]
    url_feed = url_parsed.feed
    context = {}
    context['entries'] = url_parsed0
    context['feed'] = url_feed
    return render(request, 'source/sourcecontent.html', {'JSON': context})