from django import template

register = template.Library()


@register.simple_tag()
def total_task_time(orders):
    total = 0
    for order in orders:
        tasks = order.task.all()
        for task in tasks:
            total += task.get_time_diff
    return total


@register.filter
def translate_day(value):
    translated = str(value).replace("day", "روز")
    translated = translated.replace(',', ' و')
    return translated
