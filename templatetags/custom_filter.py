from django import template

register = template.Library()

@register.filter(name='dot_separator')
def intdot(value):
    return "{:,}".format(value).replace(",", ".")
