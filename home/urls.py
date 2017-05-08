from django.conf.urls import url

from . import views

app_name = 'home'
urlpatterns = [
	# ex: /home/
	url(r'^$', views.home, name='home'),
	# ex: /home/customdata/
	url(r'^customdata/$', views.customdata, name='customuserdata'),
]