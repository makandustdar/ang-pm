from django import template

register = template.Library()


@register.filter
def get_list(dictionary, key=None):
    return dictionary.getlist(key)


@register.simple_tag
def includes(a, b):
    return str(b) in a
