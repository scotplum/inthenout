from django.shortcuts import render,  get_object_or_404

from django.contrib.auth.models import User

# Create your views here.
def home(request):
	context = {'fun':'test'}
	return render(request, 'home/index.html')