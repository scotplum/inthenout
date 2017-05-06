from django.contrib import admin

# Register your models here.
from .models import Collection, Collection_Category, Collection_Variable

# Register your models here.
admin.site.register(Collection)
admin.site.register(Collection_Category)
admin.site.register(Collection_Variable)
