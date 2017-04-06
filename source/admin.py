from django.contrib import admin

from .models import Source, Source_Variable, Source_User

# Register your models here.
admin.site.register(Source)
admin.site.register(Source_Variable)
admin.site.register(Source_User)