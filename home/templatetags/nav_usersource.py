from django import template
from source.models import Source_User, Source
from django.contrib.auth.models import User
register = template.Library()

@register.inclusion_tag('nav_usersource.html',takes_context=True)
def nav_usersource(context):
#    source_user_obj = user_object
#    nav_source_user = Source_User.objects.filter(user=source_user_obj.id)
    return context		