from django.contrib import admin

# Register your models here.
from .models import Collection, Collection_Category, Collection_Variable, User_Collection

# Register your models here.
admin.site.register(Collection)
admin.site.register(Collection_Category)
admin.site.register(Collection_Variable)
admin.site.register(User_Collection)
