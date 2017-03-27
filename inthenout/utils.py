def apicall(rss_flag, url, dict0_flag, sourcename, oauth_version, url_param):
	import requests, feedparser
	from flatten_json import flatten
	from urllib import urlencode
	context = {}
	if not url_param:
		url_call = url
	else:
		url_param = urlencode(url_param)
		url_call = url + url_param
	if rss_flag:    
		url_parsed = feedparser.parse(url)	
		context['entries'] = url_parsed.entries[0]
		context['feed'] = url_parsed.feed
	elif not rss_flag:
		url_api = {}
		if dict0_flag is False:
			context['api'] = requests.get(url_call).json()
	else:
		context['api'] = requests.get(url_call).json()[0]
	context['source'] = sourcename
	context = flatten(context, "_")
	return context