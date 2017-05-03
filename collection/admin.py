from django.contrib import admin

# Register your models here.
from .models import Collection, Collection_Category

# Register your models here.
admin.site.register(Collection)
admin.site.register(Collection_Category)
