from django.contrib import admin

from .models import Source, Source_Variable, Source_User, Source_Category

# Register your models here.
admin.site.register(Source)
admin.site.register(Source_Variable)
admin.site.register(Source_User)
admin.site.register(Source_Category)