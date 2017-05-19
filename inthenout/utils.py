import requests, feedparser
from flatten_json import flatten
from urllib import urlencode
from source.models import Source, Source_User
from collection.models import Collection, User_Collection
from django.contrib.auth.models import User
	
context = {}

def apicall(rss_flag, url, dict0_flag, sourcename, oauth_version, url_param):
	context = {}
	headers = {}
	headers['cache-control'] = 'no-cache'
	if not url_param:
		url_call = url
	else:
		url_param = urlencode(url_param)
		url_header = urlencode(headers)
		url_call = url + url_param
	if rss_flag:    
		url_parsed = feedparser.parse(url)	
		context['entries'] = url_parsed.entries[0]
		context['feed'] = url_parsed.feed
	elif not rss_flag:
		url_api = {}
		if dict0_flag is False:
			context['api'] = requests.get(url_call, headers=headers).json()
	else:
		context['api'] = requests.get(url_call, headers=headers).json()[0]
	context['source'] = sourcename
	context = flatten(context, "_")
	return context
	
def navigationlinks(request):
	#Get the object for this user and assign Source_User data
	user_object = request.user
	context['object_list'] = Source_User.objects.filter(user=user_object.id)
	context['collection_list'] = User_Collection.objects.filter(user=user_object.id)
	return context