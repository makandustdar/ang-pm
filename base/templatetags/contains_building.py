from django import template

register = template.Library()


@register.simple_tag
def contains_building(order):
    for subgroup in order.subGroup.all():
        return True if subgroup.id == 4 else False
