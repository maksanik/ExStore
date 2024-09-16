from django import template
from django.utils.http import urlencode

register = template.Library()

@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    tmp = {}
    tmp.update(kwargs)
    tmp.update(query)
    tmp.update(kwargs)
   
    
    return urlencode(tmp)