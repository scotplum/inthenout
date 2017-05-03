from django.conf.urls import url

from . import views

app_name = 'collection'
urlpatterns = [
	# ex: /collection/
	url(r'^$', views.index, name='index'),
	# ex: /collection/add/
	url(r'^add/$', views.add, name='add'),
	# ex: /collection/1/
	url(r'^(?P<collection_id>[0-9]+)/$', views.detail, name='detail'),
]