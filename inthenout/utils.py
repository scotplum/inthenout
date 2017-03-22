def apicall(rss_flag, url, dict0_flag, sourcename, oauth_version):
	import requests, feedparser
	from flatten_json import flatten
	context = {}
	if rss_flag:    
		url_parsed = feedparser.parse(url)	
		context['entries'] = url_parsed.entries[0]
		context['feed'] = url_parsed.feed
	elif not rss_flag:
		url_api = {}
		if dict0_flag is False:
			context['api'] = requests.get(url).json()
	else:
		context['api'] = requests.get(url).json()[0]
	context['source'] = sourcename
	context = flatten(context, "_")
	return context