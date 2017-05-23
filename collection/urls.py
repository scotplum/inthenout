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
	# ex: /collection/1/customdata/
	url(r'^(?P<collection_id>[0-9]+)/customdata/$', views.customdata, name='customdata'),
	# ex: /collection/1/collectsource/
	url(r'^(?P<collection_id>[0-9]+)/collectsource/$', views.collectsource, name='collectsource'),
	# ex: /collection/1/collectsource/4/
	url(r'^(?P<collection_id>[0-9]+)/collectsource/(?P<source_id>[0-9]+)/$', views.collectsourceadd, name='collectsourceadd'),
]