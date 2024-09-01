from django import template

register = template.Library()

@register.filter
def form_name(form):
    print(form.__class__.__name__, "БЕБРААААААА")
    return form.__class__.__name__