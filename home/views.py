from django.shortcuts import render,  get_object_or_404
from source.models import Source_User, Source
from django.contrib.auth.models import User


# Create your views here.
def home(request):
	user_object = request.user
	source_user_object = Source_User.objects.filter(user=user_object.id)
	context = {'object_list':source_user_object}	
	return render(request, 'home/index.html', context)