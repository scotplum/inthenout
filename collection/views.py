from django.shortcuts import render, get_object_or_404, redirect
import requests, datetime, feedparser
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from source.models import Source, Source_Variable, Source_User
from collection.models import Collection, Collection_Variable, User_Collection
from django.contrib.auth.models import User
from forms import CollectionForm, CustomCollectionDataForm
from inthenout.utils import navigationlinks

context = {}

@login_required
def index(request):
	context = navigationlinks(request)
	return render(request, 'collection/index.html',context)

@login_required
def add(request):
	context = navigationlinks(request)
	user_object = request.user
	#Form processing
	if request.method == "POST":
	    form = CollectionForm(request.POST)
	    if form.is_valid():
			post = form.save(commit=False)
			post.date_created = timezone.now()
			post.is_active = True
			post.is_public = False
			post.created_by = user_object
			post.save()
			redirecturl = '/collection/' + str(post.id) + '/'
			collection_object = Collection.objects.get(pk=post.id)
			post_uc = User_Collection(collection=collection_object, user=user_object)
			post_uc.save()
			return redirect(redirecturl)
	else:
		form_class = CollectionForm
		context['form'] = form_class
		return render(request, 'collection/add.html', context)	
	return render(request, 'collection/add.html', context)
	
@login_required
def detail(request, collection_id):
	context = navigationlinks(request)
	collection_object = Collection.objects.filter(id=collection_id)
	context['collection'] = collection_object
	context['collection_variable'] = Collection_Variable.objects.filter(collection=collection_object)
	return render(request, 'collection/detail.html', context)

@login_required
def customdata(request, collection_id):
	context = navigationlinks(request)
	collection_object = Collection.objects.filter(id=collection_id)
	context['collection'] = collection_object
	#Form Procesing
	if request.method == "POST":
	    form = CustomCollectionDataForm(request.POST)
	    if form.is_valid():
			post = form.save(commit=False)
			post.collection_id = collection_id
			post.date_created = timezone.now()
			post.is_active = True
			post.save()
			redirecturl = '/collection/' + str(collection_id) + '/'
			return redirect(redirecturl)
	else:
		form_class = CustomCollectionDataForm
		context['form'] = form_class
		return render(request, 'collection/customdata.html', context)	
	return render(request, 'collection/customdata.html', context)