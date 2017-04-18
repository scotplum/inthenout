from django.conf.urls import url

from . import views

app_name = 'emailupdate'
urlpatterns = [
	# ex: /emailupdate/
	url(r'^$', views.index, name='index'),
	# ex: /emailupdate/thanks/
	url(r'^thanks/$', views.thanks, name='thanks'),
]