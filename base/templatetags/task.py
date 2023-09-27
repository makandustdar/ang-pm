from django import template

register = template.Library()


@register.simple_tag
def published_task(current_task):
    order = current_task.order
    qs = order.task.filter(publish=True)
    return qs
