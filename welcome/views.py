from django.shortcuts import render, get_object_or_404
from inthenout.utils import navigationlinks

def index(request):
	context = navigationlinks(request)
	return render(request, 'welcome/index.html', context)	