from django.template import Library
import datetime

register = Library()


@register.simple_tag()
def is_24_hours(created_at):
    diff = datetime.datetime.utcnow().astimezone() - created_at
    if diff.days == 0:
        can_be_edited = True
    else:
        can_be_edited = False
    return can_be_edited
