from django.shortcuts import render, get_object_or_404, redirect
import requests, datetime, feedparser
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from source.models import Source, Source_Variable, Source_User
from collection.models import Collection, Collection_Variable, User_Collection, Collection_Source
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
	context['collection_source'] = Collection_Source.objects.filter(collection=collection_object).filter(is_active=True)
	collsource_count = 0
	for source in context['collection_source']:
		collsource_count = collsource_count + 1
	context['collsource_count'] = collsource_count
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
	
	
@login_required
def collectsource(request, collection_id):
	context 						= navigationlinks(request)
	user_object 					= request.user
	collection_object 				= Collection.objects.filter(id=collection_id)
	context['collection'] 			= collection_object
	context['collection_source'] 	= Collection_Source.objects.filter(collection=collection_object).filter(is_active=True)
	active_user_source 				= Source_User.objects.filter(user=user_object.id).filter(is_active=True).values_list('source_id',flat=True)
	active_collection_source 		= Collection_Source.objects.filter(collection=collection_object).filter(is_active=True).values_list('source',flat=True)
	unassigned_source 				= []
	#Determine if a source is part of the collection
	for source in active_user_source:
		if source not in active_collection_source:
			unassigned_source.append(source)
	unassigned_source = Source.objects.filter(id__in=unassigned_source)
	context['unassigned_source'] = unassigned_source
	return render(request, 'collection/collectsource.html', context)
	
def collectsourceadd(request, collection_id, source_id):
	coll_source_check = Collection_Source.objects.filter(collection=collection_id).filter(source=source_id).exists()
	collection_object = Collection.objects.get(id=collection_id)
	source_object = Source.objects.get(id=source_id)
	if not coll_source_check:
		coll_source = Collection_Source(source=source_object, collection=collection_object, date_added=timezone.now(), is_active=True)
		coll_source.save()
	else:
		coll_source = Collection_Source.objects.get(collection_id=collection_object, source_id=source_object)
		if coll_source.is_active: 
			coll_source.is_active = False
			coll_source.save()
		else:
			coll_source.is_active = True
			coll_source.save()
	redirecturl = '/collection/' + collection_id + '/collectsource/'
	return redirect(redirecturl)
