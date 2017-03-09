from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^source/', include('source.urls')),
    url(r'^emailupdate/', include('emailupdate.urls')),
    url(r'^', include('welcome.urls')),
]