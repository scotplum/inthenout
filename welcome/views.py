from django.shortcuts import render, get_object_or_404


def index(request):
	context = {
	}
	return render(request, 'welcome/index.html', context)	