from django.shortcuts import render,  get_object_or_404
from source.models import Source_User, Source
from django.contrib.auth.models import User

context = {}

# Create your views here.
def home(request):
	#Get the object for this user and assign Source_User data
	user_object = request.user
	context['object_list'] = Source_User.objects.filter(user=user_object.id)
	return render(request, 'home/index.html', context)