from django.shortcuts import render,  get_object_or_404
from source.models import Source_User, Source
from django.contrib.auth.models import User


# Create your views here.
def home(request):
	user_object = request.user.id
	source_user_object = Source_User.objects.filter(user=user_object)
	context = {'sources':source_user_object}	
	return render(request, 'home/index.html', {'source':source_user_object})