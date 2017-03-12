from django.conf.urls import url

from . import views

app_name = 'source'
urlpatterns = [
	# ex: /source/
	url(r'^$', views.index, name='index'),
	# ex: /source/quotes/
	url(r'^(?P<source_id>[0-9]+)/$', views.detail, name='detail'),
]