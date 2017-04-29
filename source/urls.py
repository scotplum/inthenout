from django.conf.urls import url

from . import views

app_name = 'source'
urlpatterns = [
	# ex: /source/
	url(r'^$', views.index, name='index'),
	# ex: /source/1/
	url(r'^(?P<source_id>[0-9]+)/$', views.detail, name='detail'),
	# ex: /source/category/..
	url(r'^category/(?P<category>[\w\-]+)/$', views.category, name='category'),
	# ex: /source/organization/..
	url(r'^organization/(?P<organization>[\w\-]+)/$', views.organization, name='organization'),
]